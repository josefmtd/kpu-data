# -*- coding: utf-8 -*-
"""
DistributionPlot.py
Created on Fri May  3 20:35:56 2019

@author: JosefStevanus
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
        
        percentageNolSatu = np.divide(cleanNolSatu, cleanTotalSuara)*100
        percentageNolSatuSeries = pd.Series(percentageNolSatu,
                                        name = "Distribusi Persentase Suara 01 di "+dataName )

        plotDistribusi, seaborn = plt.subplots()
        sns.distplot(percentageNolSatuSeries, kde=False, bins=100, ax=seaborn)
        plotDistribusi.savefig('C:/Users/JosefStevanus/Documents/GitHub/kpu-data/'+dataName+".png")
        continue
    else:
        continue

percentageNolSatuNasional = np.divide(cleanNolSatuNasional, cleanTotalSuaraNasional)*100
percentageNolSatuNasionalSeries = pd.Series(percentageNolSatuNasional,
                                        name = "Distribusi Persentase Suara 01 Nasional")

plotDistribusiNasional, seabornNasional = plt.subplots()
sns.distplot(percentageNolSatuNasionalSeries, kde=False, bins=100, ax = seabornNasional)
plotDistribusiNasional.savefig("C:/Users/JosefStevanus/Documents/GitHub/kpu-data/Nasional.png")
