# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:run3_data_relval -s RAW2DIGI,L1Reco,RECO,PAT,NANO,DQM:@rerecoZeroBiasFakeHLT+@miniAODDQM+@nanoAODDQM --datatier RECO,MINIAOD,NANOAOD,DQMIO --eventcontent RECO,MINIAOD,NANOEDMAOD,DQM --data --process reRECO --scenario pp --era Run3_2023 --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run3 --hltProcess reHLT -n 100 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

process = cms.Process('reRECO',Run3_2023)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PAT_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step2.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.RECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:step3_inMINIAOD.root'),
    outputCommands = process.MINIAODEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVerticesWithBS__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

process.NANOEDMAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inNANOEDMAOD.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.Applications.ConfigBuilder import ConfigBuilder
process.DQMOfflineMiniAOD.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineNanoAOD.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineMuon.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineHcal.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineHcal2.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineJetMET.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineEcal.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineEGamma.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineL1TMuon.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineL1TEgamma.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineCTPPS.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineDCS.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMMessageLoggerSeq.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineTrackerStripMinBias.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineTrackerPixel.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineTrackingMinBias.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineL1T.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineBeam.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflineCASTOR.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
process.DQMOfflinePhysics.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",), verbose = False))
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_relval', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_BadPFMuonDzFilter = cms.Path(process.BadPFMuonDzFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_hfNoisyHitsFilter = cms.Path(process.hfNoisyHitsFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.nanoAOD_step = cms.Path(process.nanoSequence)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineMiniAOD)
process.dqmoffline_1_step = cms.EndPath(process.DQMOfflineNanoAOD)
process.dqmoffline_2_step = cms.EndPath(process.DQMOfflineMuon)
process.dqmoffline_3_step = cms.EndPath(process.DQMOfflineHcal)
process.dqmoffline_4_step = cms.EndPath(process.DQMOfflineHcal2)
process.dqmoffline_5_step = cms.EndPath(process.DQMOfflineJetMET)
process.dqmoffline_6_step = cms.EndPath(process.DQMOfflineEcal)
process.dqmoffline_7_step = cms.EndPath(process.DQMOfflineEGamma)
process.dqmoffline_8_step = cms.EndPath(process.DQMOfflineL1TMuon)
process.dqmoffline_9_step = cms.EndPath(process.DQMOfflineL1TEgamma)
process.dqmoffline_10_step = cms.EndPath(process.DQMOfflineCTPPS)
process.dqmoffline_11_step = cms.EndPath(process.DQMOfflineDCS)
process.dqmoffline_12_step = cms.EndPath(process.DQMMessageLoggerSeq)
process.dqmoffline_13_step = cms.EndPath(process.DQMOfflineTrackerStripMinBias)
process.dqmoffline_14_step = cms.EndPath(process.DQMOfflineTrackerPixel)
process.dqmoffline_15_step = cms.EndPath(process.DQMOfflineTrackingMinBias)
process.dqmoffline_16_step = cms.EndPath(process.DQMOfflineL1T)
process.dqmoffline_17_step = cms.EndPath(process.DQMOfflineBeam)
process.dqmoffline_18_step = cms.EndPath(process.DQMOfflineCASTOR)
process.dqmoffline_19_step = cms.EndPath(process.DQMOfflinePhysics)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.dqmofflineOnPAT_1_step = cms.EndPath(process.PostDQMOfflineMiniAOD)
process.dqmofflineOnPAT_2_step = cms.EndPath(process.PostDQMOffline)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.MINIAODoutput_step = cms.EndPath(process.MINIAODoutput)
process.NANOEDMAODoutput_step = cms.EndPath(process.NANOEDMAODoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadPFMuonDzFilter,process.Flag_hfNoisyHitsFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.nanoAOD_step,process.dqmoffline_step,process.dqmoffline_1_step,process.dqmoffline_2_step,process.dqmoffline_3_step,process.dqmoffline_4_step,process.dqmoffline_5_step,process.dqmoffline_6_step,process.dqmoffline_7_step,process.dqmoffline_8_step,process.dqmoffline_9_step,process.dqmoffline_10_step,process.dqmoffline_11_step,process.dqmoffline_12_step,process.dqmoffline_13_step,process.dqmoffline_14_step,process.dqmoffline_15_step,process.dqmoffline_16_step,process.dqmoffline_17_step,process.dqmoffline_18_step,process.dqmoffline_19_step,process.dqmofflineOnPAT_step,process.dqmofflineOnPAT_1_step,process.dqmofflineOnPAT_2_step,process.RECOoutput_step,process.MINIAODoutput_step,process.NANOEDMAODoutput_step,process.DQMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
from Configuration.DataProcessing.RecoTLR import customisePostEra_Run3 

#call to customisation function customisePostEra_Run3 imported from Configuration.DataProcessing.RecoTLR
process = customisePostEra_Run3(process)

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 

#call to customisation function nanoAOD_customizeCommon imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# End of customisation functions

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllData 

#call to customisation function miniAOD_customizeAllData imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllData(process)

# End of customisation functions

# Customisation from command line

process.patTrigger.processName = "reHLT"
process.slimmedPatTrigger.triggerResults= cms.InputTag( 'TriggerResults::reHLT' )
process.patMuons.triggerResults= cms.InputTag( 'TriggerResults::reHLT' )
 
process.unpackedPatTrigger.triggerResults= cms.InputTag( 'TriggerResults::reHLT' )

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
