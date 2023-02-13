import CRABClient
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'unsupervisedZToeeAnalysis_Feb2023_data_test'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ntuplize.py'

config.Data.inputDataset = '/ZeroBias/Run2018D-UL2018_MiniAODv2-v1/MINIAOD'
config.Data.secondaryInputDataset = '/ZeroBias/Run2018D-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 1
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'unsupervisedZToeeAnalysis_Feb2023_data_test'
config.Data.partialDataset = True

config.Site.storageSite = 'T2_US_Wisconsin'