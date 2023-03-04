#!/usr/bin/env python3
import ROOT

class sample:
    def __init__(self, listOfFiles:list):
        self.listOfFiles = listOfFiles

        self.chain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
        self.uGTChain = ROOT.TChain('uGTModelNtuplizer/uGTModelOutput')
        self.eventChain = ROOT.TChain('l1EventTree/L1EventTree')
        self.electronChain = ROOT.TChain('electronInformationAnalyzer/ElectronInformation')

        allChains = [
            self.chain,
            self.uGTChain,
            self.eventChain,
            self.electronChain
        ]

        for fileName in listOfFiles:
            for chain in allChains:
                chain.Add(fileName)
        
        self.chain.AddFriend(self.uGTChain)
        self.chain.AddFriend(self.eventChain)
        self.chain.AddFriend(self.electronChain)
    
    def GetEntry(self, entryNum: int):
        self.chain.GetEntry(entryNum)
    
    def GetEntries(self) -> int:
        return self.chain.GetEntries()