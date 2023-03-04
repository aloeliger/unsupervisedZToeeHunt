#!/usr/bin/env python3
from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloelige/ZeroBias/unsupervisedZToeeAnalysis_26Feb2023_ZB2018D/230226_224835/'
subDirs = (1,2,3,4)
listOfFiles = []

for subDir in subDirs:
    path = f'{hdfsPath}/000{subDir}/'

    #listOfFiles += [path+'/' + x for x in os.listdir(path)]
    listOfFiles += [path+'/' + x for x in os.listdir(path)[:10]]

zeroBiasDSample = sample(listOfFiles)