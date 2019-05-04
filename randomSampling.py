# -*- coding: utf-8 -*-
"""
RandomSampling.py
Created on Sat May  4 09:45:12 2019

@author: DarwinHarianto
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

directory = 'C:/Users/JosefStevanus/Documents/GitHub/kpu-data/'
data = {}
cleanNolSatuNasional = []
cleanNolDuaNasional = []
cleanTotalSuaraNasional = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        dataName = filename[:-4]
        data[dataName] = pd.read_csv(filename)
        
        nolSatu = data[dataName]["01 KPU"]        
        nolDua = data[dataName]["02 KPU"]
        cleanNolSatu = []
        cleanNolDua = []

        for x in range(len(nolSatu)):
            if nolSatu[x] == 0 and nolDua[x] == 0:
                continue
            else:
                cleanNolSatu.append(nolSatu[x])
                cleanNolDua.append(nolDua[x])
        
        cleanTotalSuara = np.add(cleanNolSatu, cleanNolDua)
        
        cleanNolSatuNasional += cleanNolSatu
        cleanNolDuaNasional += cleanNolDua
        cleanTotalSuaraNasional += cleanTotalSuara.tolist() 
        continue
    else:
        continue

percentageNolSatuNasional = np.divide(cleanNolSatuNasional, cleanTotalSuaraNasional)*100
percentageNolSatuNasionalSeries = pd.Series(percentageNolSatuNasional,
                                        name = "Distribusi Persentase Suara 01 Nasional")

plotDistribusiNasional, seabornNasional = plt.subplots()
sns.distplot(percentageNolSatuNasionalSeries, kde=False, bins=100, ax = seabornNasional)
plotDistribusiNasional.savefig("C:/Users/JosefStevanus/Documents/GitHub/kpu-data/Nasional.png")

randomSample = random.sample(range(len(cleanTotalSuaraNasional)), 2000)

nolSatuRandomSample = []
nolDuaRandomSample = []
totalSuaraRandomSample = []

for x in randomSample:
    nolSatuRandomSample.append(cleanNolSatuNasional[x])
    nolDuaRandomSample.append(cleanNolDuaNasional[x])
    totalSuaraRandomSample.append(cleanTotalSuaraNasional[x])

percentageNolSatuRandomSample = np.divide(nolSatuRandomSample, totalSuaraRandomSample)*100
percentageNolSatuRandomSampleSeries = pd.Series(percentageNolSatuRandomSample, 
                                                name = "Distribusi Persentase Suara 01 Random Sample")

meanNolSatu = np.sum(nolSatuRandomSample)/np.sum(totalSuaraRandomSample)*100
meanNolDua = 100 - meanNolSatu
standardError = np.std(percentageNolSatuRandomSample)/np.sqrt(len(randomSample))

meanNolSatuNasional = np.sum(cleanNolSatuNasional)/np.sum(cleanTotalSuaraNasional)*100
meanNolDuaNasional = 100 - meanNolSatuNasional
standardErrorNasional = np.std(percentageNolSatuNasional)/np.sqrt(len(cleanTotalSuaraNasional))

plotDistribusiNasionalRandomSample, ax = plt.subplots(2,1)
sns.distplot(percentageNolSatuRandomSampleSeries, bins=100, ax = ax[0])
sns.distplot(percentageNolSatuNasionalSeries, bins=100, ax = ax[1])
plotDistribusiNasionalRandomSample.suptitle('{:.2f}% vs {:.2f}% Real Count Sementara \n {:.2f}% vs {:.2f}%Random Sampling dengan MOE = +/-{:.2f}%'.format(meanNolSatuNasional, meanNolDuaNasional, meanNolSatu, meanNolDua, standardError*2.58))