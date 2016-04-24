# -*- coding: utf-8 -*-

# Owner: Cheng.Yan cheng.yan@nyu.edu
# Des: one time running code for process input data


import csv


def dataClean():
    # K-O列为卖五档，P-T为买五档，U-Y为卖五量，Z-AD为买五量
    with open( '20160405Option.csv','rb') as f:
        reader = csv.reader(f)
        res = [ line for line in reader ]
    return res

for line in dataClean():
    print line
    break