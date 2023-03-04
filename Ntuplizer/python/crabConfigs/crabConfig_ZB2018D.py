import CRABClient
from CRABClient.UserUtilities import config
import os

config = config()

config.General.requestName = 'unsupervisedZToeeAnalysis_26Feb2023_ZB2018D'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/unsupervisedZToeeHunt/Ntuplizer/python/ntuplize.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/ZeroBias/Run2018D-UL2018_MiniAODv2-v1/MINIAOD'
config.Data.secondaryInputDataset = '/ZeroBias/Run2018D-v1/RAW'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'FileBased'
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1080
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'unsupervisedZToeeAnalysis_26Feb2023_ZB2018D'

config.Site.storageSite = 'T2_US_Wisconsin'