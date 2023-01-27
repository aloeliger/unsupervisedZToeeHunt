import subprocess

import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing('analysis')
options.parseArguments()

def attachL1EmulationSequences(theProcess):
    pass

def attachL1NtupleSequences (theProcess):
    from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
    associatePatAlgosToolsTask(theProcess)

def attachMiniAODAnalysisSequences(theProcess):
    pass

