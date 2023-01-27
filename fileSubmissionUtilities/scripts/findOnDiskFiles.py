#Script that will take a dataset, or a dasquery for multiple datasets
#Figure out which which files are on disk, and where,
#Then create a json with this information available

import argparse
import json
import subprocess
from tqdm import tqdm

def runDAS(query):
    try:
        completeProcess = subprocess.run(query, capture_output=True, shell=True)
    except:
        raise RuntimeError('failed to run query:'+' '.join(query))
    
    if (completeProcess.returncode != 0 or completeProcess.stderr.decode() != ''):
        raise RuntimeError(f'dasgoclient call exited with non-zero status or had another error: \n{completeProcess.stderr.decode()}')
    return completeProcess

def queryDASforDataset(theQueryString):
    theQuery = f'dasgoclient --query="dataset={theQueryString}"'

    completeProcess = runDAS(theQuery)
    
    datasets = completeProcess.stdout.decode().split('\n')
    datasets = datasets[:len(datasets)-1] #remove the trailing empty string
    return datasets

def locateDiskSites(dataset):
    theQuery = f'dasgoclient --query="site dataset={dataset}"'

    completeProcess = runDAS(theQuery)

    sites = completeProcess.stdout.decode().split('\n')
    sites = sites[:len(sites)-1]

    sites = [site for site in sites if 'Tape' not in site]

    return sites

def findFilesAtSite(dataset,site):
    theQuery = f'dasgoclient --query="file site={site} dataset={dataset}"'

    completeProcess = runDAS(theQuery)

    files = completeProcess.stdout.decode().split('\n')
    files = files[:len(files)-1]

    return files

def printFileStructure(theDict):
    for dataset in theDict:
        print(dataset)
        for site in theDict[dataset]:
            print(f'\t\u2514 {site}: {len(theDict[dataset][site])} files')

def main(args):
    fileDictionary = {}
    #first let's get a series of datasets that match our query
    print('Locating datasets...')
    datasets = queryDASforDataset(args.datasetQuery)
    print(f'Found {len(datasets)} Datasets matching query')
    #print(datasets)
    #now that we have those, we should poll das on what sites each is located in.
    print('Finding sites and files...')
    for dataset in tqdm(datasets, desc='Datasets'):
        #print(locateDiskSites(dataset))
        fileDictionary[dataset] = {}
        diskSites = locateDiskSites(dataset)
        for site in tqdm(diskSites, leave=False, desc='Sites'):
            fileDictionary[dataset][site] = findFilesAtSite(dataset, site)
    printFileStructure(fileDictionary)

    with open(args.outputJson, 'w') as jsonFile:
        json.dump(fileDictionary, jsonFile, indent=4)

    return 0
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='das to json query tool for files on disk')

    parser.add_argument('--datasetQuery', required=True, help='dataset to query for and check for on disk files')
    parser.add_argument('--outputJson', required=True, help='place to put the final json')

    args = parser.parse_args()

    exitCode = main(args)

    exit(exitCode)