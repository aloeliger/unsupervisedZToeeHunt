#take a map of RAW files on disk with a list of MiniAOD children, and turn it into a 
#map of miniAOD files to their RAW parents

import json
import argparse
from tqdm import tqdm

def main(args):
    with open(args.inputJSON, 'r') as jsonFile:
        rawMap = json.load(jsonFile)

    miniAODMap = {}
    for dataset in tqdm(rawMap, desc='Dataset'):
        miniAODMap[dataset] = {}
        for fileName in tqdm(rawMap[dataset],desc='Raw Files', leave=False):
            for miniAODFile in rawMap[dataset][fileName]:
                if miniAODFile not in miniAODMap[dataset].keys():
                    miniAODMap[dataset][miniAODFile] = []
                if fileName not in miniAODMap[dataset][miniAODFile]:
                    miniAODMap[dataset][miniAODFile].append(fileName)

    with open(args.outputJSON, 'w') as jsonFile:
        json.dump(jsonFile, miniAODMap, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a submission JSON')
    
    parser.add_argument('--inputJSON', required=True, help='input file mapping raw to miniAOD')
    parser.add_argument('--outputJSON', required=True, help='output file mapping miniAOD to raw')

    args = parser.parse_args()

    main(args)