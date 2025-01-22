# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --process reHLT -s L1REPACK:Full,HLT:@relval2023 --conditions auto:run3_hlt_relval --data --eventcontent FEVTDEBUGHLT --datatier FEVTDEBUGHLT --era Run3_2023 -n 100 --filein filelist:step1_dasquery.log --lumiToProcess step1_lumiRanges.log --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

process = cms.Process('reHLT',Run3_2023)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorRepack_Full_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/06f56347-618a-49ac-b2b7-d7269d0a8984.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/08207ceb-2b76-4ee4-83f6-f511780a18a1.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/0d11f751-9e43-4990-8197-bdb214d61f16.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/0e72f9ae-8e07-400e-a3ee-eb29f8e0ce4f.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/0ed4db55-497a-442d-8d06-cc83bf5f9149.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/126e3555-744d-454e-ac7a-2d90eeb49b18.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/13316c45-9502-421f-95ac-455687a813dc.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/133f3d60-bae0-4afc-b506-f6708d7115d8.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/197c8585-153a-4e05-b7a3-296990932598.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/1f0c229d-dbb3-48f0-a86d-ac666ebbb04a.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/29f53c65-9558-4074-b89c-0ebd3b24c9c8.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/2e2efae1-b780-4e0f-8189-3df80c8e270d.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/2ecc7fdf-96b9-4206-8334-f504a64c055e.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/2fd9e52f-33f7-4e76-abd1-b82b34ab94b0.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/339d77a1-7b0e-4b2a-a636-5c1a0bd9f49a.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/36fd4ed9-94b3-48d2-af52-f715c7951643.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/3a43e8fe-1a92-4614-95b0-91a64daaaee0.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/3ec5337c-6ed3-4533-933e-daa0c5becb47.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/44eefadd-11d2-4f8c-bf98-241f728e3aa1.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/4decfa90-5ebe-4d88-80e8-80492d7b03cc.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/5ac4b525-e90b-4863-b903-96c5e08d86a6.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/5d8470b2-b807-443e-846f-cc2a7d9eaa7c.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/6488fc28-bc8b-45b6-a8f0-0cdccf396192.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/66553f31-89b4-4d7a-85c7-0d6ed695069f.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/68aa09c2-58bd-4598-80c5-16c9db5b84e3.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/7097e9a0-e5c2-4b2a-8fe6-50a68ed7b85d.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/73e11a8d-7311-4c0e-ad0c-9117d24d1f33.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/7dc58874-035a-44d3-91f9-51944545a669.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/8064cc53-4504-4246-8e4c-43d734040ca8.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/84c8ab1f-9380-4d3d-9754-7ef5c057d54a.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/8bab0a64-12f8-482e-bd31-4540837f8269.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/8cf6362a-9763-4596-83f0-ceb9742a86e9.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/8ed6976c-ebb6-4e32-884b-ec0612f0f38f.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/94a2557f-dd5c-458b-8ca4-a3044510a839.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/9cd0a734-d707-44e7-9fd2-ff1dae86f84f.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/9fe2c9f9-cf12-49ca-8b2d-f344c136b00d.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/a59339b1-00a3-474b-85f8-06419062a5fa.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/aa253220-1066-42c8-aac8-b392a670ec24.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/ae074aa2-f438-4db7-ae83-1cd28f79fe35.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/aebf07fa-af11-43b8-bfa8-de1101f0e415.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/af497bad-066f-4cc0-94d4-bd3d37b0942c.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/b98fa6fc-803b-423f-8669-ef101ca4eb54.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/bfd3b3cb-06fd-443f-b193-4ca6165834c4.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/c5cc6fcf-0b6b-4069-ad82-159bbac763fc.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/c748aadc-79d9-41e4-91a3-6dee2950e952.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/c8dce956-a135-42d5-99a1-9fc70c1735ba.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/cb2fd4df-52e3-4b00-83bf-8be13464e198.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/cfe511a2-5e6a-467b-84b4-d95013d14598.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/d5be92bb-910a-4afb-a4cc-019b2f3965b1.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/d66fb324-738c-4469-a0a2-c7195d863aa8.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/d98c0664-7fa4-4e60-a694-42f6b28777c3.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/e13c93a8-7caf-4a85-ae7d-db09870e0890.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/e393b196-616d-43fb-929b-ec6ea95426b6.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/e50e95f1-d63f-479d-b761-09dd0d98716c.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/e6d466bd-2f8d-4ab1-9a2f-9d76def9ad98.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/ec71599f-f3d0-4add-996c-72fe46c4e941.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/f0e9f45c-b5a5-4466-a0d6-a43ed7a1d53f.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/f18f2800-7e17-4902-a55c-2bf38f24ef81.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/f79b5824-558c-473a-8a52-6d666363e19b.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/f7dfa7ef-81d0-487b-9877-55fd39b71808.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/f9bb8b34-8bad-49d8-9ad5-b872973f533f.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/fae5a5dd-dc7c-4519-878f-4590fd406722.root',
        '/store/data/Run2023C/ZeroBias/RAW/v1/000/367/131/00000/ff791724-17a7-42bf-817f-2559cda7020d.root'
    ),
    lumisToProcess = cms.untracked.VLuminosityBlockRange("367131:1-367131:149"),
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
    annotation = cms.untracked.string('step2 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('FEVTDEBUGHLT'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_hlt_relval', '')

# Path and EndPath definitions
process.L1RePack_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.L1RePack_step)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
