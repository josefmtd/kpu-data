# -*- coding: utf-8 -*-
"""
RandomSampling.py
Created on Sat May  4 09:45:12 2019

@author: JosefStevanus
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:35:56 2019

@author: JosefStevanus
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

directory = 'kpu-data-master/'
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
        
        percentageNolSatu = np.divide(cleanNolSatu, cleanTotalSuara)*100
        percentageNolSatuSeries = pd.Series(percentageNolSatu,
                                        name = "Distribusi Persentase Suara 01 di "+dataName )

        plotDistribusi, seaborn = plt.subplots()
        sns.distplot(percentageNolSatuSeries, kde=False, bins=100, ax=seaborn)
        plotDistribusi.savefig('kpu-data-master/'+dataName+".png")
        continue
    else:
        continue

percentageNolSatuNasional = np.divide(cleanNolSatuNasional, cleanTotalSuaraNasional)*100
percentageNolSatuNasionalSeries = pd.Series(percentageNolSatuNasional,
                                        name = "Distribusi Persentase Suara 01 Nasional")

plotDistribusiNasional, seabornNasional = plt.subplots()
sns.distplot(percentageNolSatuNasionalSeries, kde=False, bins=100, ax = seabornNasional)
plotDistribusiNasional.savefig("kpu-data-master/Nasional.png")

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

plotDistribusiNasionalRandomSample, ax = plt.subplots(2,1)
sns.distplot(percentageNolSatuRandomSampleSeries, kde=False, bins=100, ax = ax[0])
sns.distplot(percentageNolSatuNasionalSeries, kde=False, bins=100, ax = ax[1])


meanNolSatu = np.sum(nolSatuRandomSample)/np.sum(totalSuaraRandomSample)*100
meanNolDua = 100 - meanNolSatu
standardError = np.std(percentageNolSatuRandomSample)/np.sqrt(len(randomSample))

print("RandomSample")
print("Suara 01:", str(meanNolSatu) + "%")
print("Suara 02:", str(meanNolDua) + "%")
print("Standard Error:", str(standardError)+ "%")
print("Margin of Error (99% CL):", str(standardError*2.58) + "%")

meanNolSatuNasional = np.sum(cleanNolSatuNasional)/np.sum(cleanTotalSuaraNasional)*100
meanNolDuaNasional = 100 - meanNolSatuNasional
standardErrorNasional = np.std(percentageNolSatuNasional)/np.sqrt(len(cleanTotalSuaraNasional))

print("")

print("Real Count Data")
print("Suara 01:", str(meanNolSatuNasional) + "%")
print("Suara 02:", str(meanNolDuaNasional) + "%")
print("Standard Error:", str(standardErrorNasional) + "%")
print("Margin of Error (99% CL):", str(standardErrorNasional*2.58) + "%")
