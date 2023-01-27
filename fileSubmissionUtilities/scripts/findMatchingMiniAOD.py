#This script will take an existing list of RAW files on disk, and find the 
#miniAOD files for the corresponding run

import argparse
import json
import subprocess
from tqdm import tqdm
from findOnDiskFiles import runDAS
import re

def locateMiniAOD(rawFile, dataset):
    #given a raw file, we should be able to quickly and easily find all of it's children
    childQuery = f'dasgoclient --query="child file={rawFile}"'

    completeProcess = runDAS(childQuery)

    fileList = completeProcess.stdout.decode().split('\n')
    fileList = fileList[:len(fileList)-1]

    miniAODList = []

    for fileName in fileList:
        if 'MINIAOD' in fileName:
            datasetTag = re.search('(?<=/MINIAOD/).*?(?=/)', fileName).group(0)
            #datasets aren't explicitly filled out in the file names, but this should be close enough
            if datasetTag in dataset and fileName not in miniAODList:
                miniAODList.append(fileName)
    return miniAODList 

def printMatchingDictionaryInformation(matchingDict, dataset):
    for dataset in matchingDict:
        print(dataset)

        totalRawFiles = 0.0
        rawFilesWithMatches = 0.0

        for fileName in matchingDict:
            totalRawFiles += 1.0
            if matchingDict[dataset][fileName] != []:
                rawFilesWithMatches += 1.0
        print(f'\t\u2514Raw files with MiniAOD matches: {rawFilesWithMatches/totalRawFiles:3.2%}')

        fileQuery = f'dasgoclient --query="file dataset={dataset}"'

        completeProcess = runDAS(fileQuery)

        fileList = completeProcess.stdout.decode().split('\n')
        fileList = fileList[:len(fileList)-1]

        miniAODList = []

        for fileName in matchingDict:
            for miniAODFile in matchingDict[dataset][fileName]:
                if miniAODFile not in miniAODList:
                    miniAODList.append(miniAODFile)
        print(f'\t\u2514MiniAOD percentage of total dataset: {float(len(miniAODList))/float(len(fileList)):3.2%}')

def main(args):
    with open(args.rawJson, 'r') as jsonFile:
        fileDictionary = json.load(jsonFile)

    matchingDict = {}

    print('Finding MiniAOD counterparts...')
    for dataset in tqdm(fileDictionary,desc='Datasets'):
        matchingDict[dataset]={}
        for site in tqdm(fileDictionary[dataset],desc='Sites',leave=False):
            for fileName in tqdm(fileDictionary[dataset][site],desc='Files',leave=False):
                if fileName in matchingDict[dataset].keys():
                    continue
                matchingDict[dataset][fileName] = locateMiniAOD(fileName, args.counterpartDataset)

    print('Dumping info to JSON...')
    with open(args.outputJson, 'w') as jsonFile:
        json.dump(matchingDict, jsonFile, indent=4)

    print('Fetching information about the matches...')    
    printMatchingDictionaryInformation(matchingDict, args.counterpartDataset)
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Find miniAOD on disk to match RAW on disk')

    parser.add_argument('--rawJson', required=True, help='raw json to find counterparts to')
    parser.add_argument('--counterpartDataset', required=True, help='dataset to search for counterparts in')
    parser.add_argument('--outputJson', required=True, help='output json')

    args = parser.parse_args()

    main(args)