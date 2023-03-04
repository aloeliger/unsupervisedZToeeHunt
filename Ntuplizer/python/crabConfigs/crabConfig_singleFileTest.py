import CRABClient
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'unsupervisedZToeeAnalysis_Feb2023_data_test'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/hep.wisc.edu/cms/aloeliger/anomalyTriggerWork/CMSSW_12_4_3/src/unsupervisedZToeeHunt/Ntuplizer/python/ntuplize.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/ZeroBias/Run2018D-UL2018_MiniAODv2-v1/MINIAOD'
config.Data.secondaryInputDataset = '/ZeroBias/Run2018D-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 5
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'unsupervisedZToeeAnalysis_Feb2023_data_test'
config.Data.partialDataset = True

config.Site.storageSite = 'T2_US_Wisconsin'