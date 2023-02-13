#quick config to test the loading and running of multiple datasets 
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process = cms.Process("USERTEST",Run2_2018)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.MessageLogger.suppressWarning = cms.untracked.vstring(
    'l1UpgradeTree',
    'l1UpgradeEmuTree',
    'l1UpgradeTfMuonShowerTree', 
    'emtfSL1TMuonEndCapTrackProducertage2Digis', 
    'simEmtfDigis', #'L1TMuonEndCapTrackProducer'
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Run2018D/ZeroBias/MINIAOD/UL2018_MiniAODv2-v1/00000/64E7DAC6-FBB3-9541-90A1-AFF17473416D.root'),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/72AD17AF-09A3-E811-A283-FA163ED5E288.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/D60E376B-09A3-E811-9A37-FA163E41F45F.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/712/00000/681A3C04-8DA7-E811-956E-02163E00F6C4.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/712/00000/D45C40F7-8CA7-E811-9280-FA163E8B9DC9.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/207B7CCD-1EA3-E811-BD90-FA163E0EB820.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/64E2701B-1DA3-E811-9E8C-FA163E336AEF.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/C4C4DC58-1DA3-E811-BA05-FA163E5CBB1F.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/34E8A6EB-04A3-E811-9BCF-FA163EE124FD.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/9A9192F5-04A3-E811-8601-FA163E6C5CF2.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/9C7EAAA8-04A3-E811-98CB-FA163E6E9B93.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/9E060BB9-04A3-E811-B1E5-FA163EE9CA17.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/4666F616-1DA3-E811-8B36-FA163E605AB1.root', 
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/64E2701B-1DA3-E811-9E8C-FA163E336AEF.root', #duplicate
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/730/00000/18521EC0-1BA7-E811-B970-02163E016618.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/730/00000/FC28A0AB-1BA7-E811-B184-FA163E363203.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/0E0E9EEB-17A3-E811-9C9A-FA163E82AE3E.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/507D7B2E-19A3-E811-83F7-02163E00B19F.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/709/00000/1C7DBACB-A3A7-E811-BA8B-FA163E45E102.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/0A5248F0-05A3-E811-BC85-FA163E552AFD.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/5AEDF8F9-05A3-E811-ABAE-02163E019E95.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/7A54A156-06A3-E811-89AE-FA163E6FA269.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/361CB633-1DA3-E811-A990-02163E01773E.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/DC00D8A3-1EA3-E811-947D-FA163EDA08D4.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/E0D9CFF8-1CA3-E811-BB23-FA163EB99920.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/0C9D07F9-04A3-E811-A969-FA163ECFEB66.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/4CCB66C2-04A3-E811-93F4-FA163E881A5A.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/9E060BB9-04A3-E811-B1E5-FA163EE9CA17.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/F4872FE0-04A3-E811-8C7A-FA163E2952B3.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/8A21933B-07A3-E811-B3EC-02163E019F0E.root', 
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/9A9192F5-04A3-E811-8601-FA163E6C5CF2.root', #duplicate
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/B2D51BA7-04A3-E811-9020-FA163E8CF580.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/EE92DCF9-06A3-E811-A620-FA163E9BB4E9.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/0612E2BF-0DA3-E811-9F6F-FA163E9A7438.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/434/00000/F45FE6BB-0DA3-E811-8987-FA163E9BE5CE.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/732/00000/2E769FA4-94A7-E811-AFB5-FA163EFA689B.root', 
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/321/732/00000/E0B6A6B4-94A7-E811-AF66-FA163E89EFE9.root'
                            )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
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
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Schedule definition
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

process.schedule = cms.Schedule(process.raw2digi_step, process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 1
process.options.numberOfStreams = 1
process.options.numberOfConcurrentLuminosityBlocks = 1
process.options.eventSetup.numberOfConcurrentIOVs = 1
if hasattr(process, 'DQMStore'): process.DQMStore.assertLegacySafe=cms.untracked.bool(False)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_3 

#call to customisation function L1TSettingsToCaloParams_2018_v1_3 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2018_v1_3(process)

#load up our ntuplization stuff and append it on to the end of the schedule
process.load('L1Trigger.L1TCaloLayer1.uct2016EmulatorDigis_cfi')
process.CaloSummaryPath = cms.Path(process.uct2016EmulatorDigis)
process.schedule.append(process.CaloSummaryPath)

process.load('L1Trigger.anomalyTriggerSkunkworks.uGTADEmulator_cfi')
process.uGTEmulationPath = cms.Path(process.uGTADEmulator)
process.schedule.append(process.uGTEmulationPath)

process.load('L1Trigger.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi')
process.L1TCaloSummaryTestNtuplizer.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')
process.L1TCaloSummaryTestNtuplizer.hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis')

process.load('L1Trigger.anomalyTriggerSkunkworks.L1TTriggerBitsNtuplizer_cfi')
process.L1TTriggerBitsNtuplizer.verboseDebug= cms.bool(False)

process.load('L1Trigger.anomalyTriggerSkunkworks.boostedJetTriggerNtuplizer_cfi')

process.load('L1Trigger.anomalyTriggerSkunkworks.uGTModelNtuplizer_cfi')

process.load('unsupervisedZToeeHunt.Ntuplizer.electronInformationAnalyzer_cfi')

#output file service
process.TFileService = cms.Service(
	"TFileService",
	fileName = cms.string("analysisNtuple.root")
    #fileName = cms.string(options.outputFile)
)

process.NtuplePath = cms.Path(
                                process.L1TCaloSummaryTestNtuplizer +
                                process.L1TTriggerBitsNtuplizer +
                                process.boostedJetTriggerNtuplizer +
                                process.uGTModelNtuplizer
                              )
process.schedule.append(process.NtuplePath)

process.MiniAODNtuplePath = cms.Path(
    process.electronInformationAnalyzer
)

process.schedule.append(process.MiniAODNtuplePath)

print(f'{"Schedule":^50}')
print(f'{"----------":^50}')
print(process.schedule)
print(f'{"----------":^50}')
print([x for x in process.schedule])

#Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)