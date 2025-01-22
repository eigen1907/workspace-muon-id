import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.parseArguments()

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023
process = cms.Process('RECO', Run3_2023)

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')       # 이미 완료됐다면 주석처리
process.load('Configuration.StandardSequences.L1Reco_cff')         # 이미 완료됐다면 주석처리
process.load('Configuration.StandardSequences.Reconstruction_cff')
#process.load('Configuration.StandardSequences.RecoSim_cff')

process.load('Configuration.StandardSequences.EndOfProcess_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2023_realistic', '')

inputFileName = options.inputFiles if len(options.inputFiles)>0 else ['file:preReco.root']
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(inputFileName))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step   = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction) 
#process.recosim_step  = cms.Path(process.recosim)

process.endjob_step = cms.EndPath(process.endOfProcess)

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outputFile if options.outputFile else 'reco.root'),
    dataset = cms.untracked.PSet(
        #dataTier = cms.untracked.string('RECOSIM'),
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    outputCommands = process.RECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)

process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.L1Reco_step,
    process.reconstruction_step,
    #process.recosim_step,
    process.endjob_step,
    process.RECOoutput_step
)

from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC
process = customizeHLTforMC(process)

from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
