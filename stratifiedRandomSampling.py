# -*- coding: utf-8 -*-
"""
StratifiedRandomSampling.py
Created on Sat May  4 09:45:12 2019

@author: JosefStevanus
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:35:56 2019

@author: JosefStevanus
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

class dataPemilu:
    def __init__(self, filename, dataSource):
        self.nolSatu = []
        self.nolDua = []
        self.totalSuara = []
        self.sampleNolSatu = []
        self.sampleNolDua = []
        self.sampleTotalSuara = []
        self.filename = filename
        self.getRawData(dataSource)
        self.cleanData()

    def getRawData(self, dataSource):
        data = pd.read_csv(self.filename)
        if dataSource == "KPU":
            self.nolSatu = data["01 KPU"]
            self.nolDua = data["02 KPU"]
        elif dataSource == "KawalPemilu":
            self.nolSatu = data ["01 KawalPemilu"]
            self.nolDua = data ["02 KawalPemilu"]
        else:
            print("Source data does not exist")
        self.totalSuara = np.add(self.nolSatu, self.nolDua)

    def cleanData(self):
        cleanNolSatu = []
        cleanNolDua = []
        for x in range (len(self.totalSuara)):
            if self.nolSatu[x] == 0 and self.nolDua[x] == 0:
                continue
            else:
                cleanNolSatu.append(self.nolSatu[x])
                cleanNolDua.append(self.nolDua[x])
        
        self.nolSatu = cleanNolSatu
        self.nolDua = cleanNolDua
        self.totalSuara = np.add(cleanNolSatu, cleanNolDua).tolist()
    
    def randomSample(self, sampleSize):
        listSample = random.sample(range(len(self.totalSuara)), sampleSize)
        for x in listSample:
            self.sampleNolSatu.append(self.nolSatu[x])
            self.sampleNolDua.append(self.nolDua[x])
            self.sampleTotalSuara.append(self.totalSuara[x])
        
aceh = dataPemilu("Aceh.csv", "KPU")
bali = dataPemilu("Bali.csv", "KPU")
banten = dataPemilu("Banten.csv", "KPU")
bengkulu = dataPemilu("Bengkulu.csv", "KPU")
daerahIstimewaYogyakarta = dataPemilu("DaerahIstimewaYogyakarta.csv", "KPU")
daerahKhususIbukotaJakarta = dataPemilu("DaerahKhususIbukotaJakarta.csv", "KPU")
gorontalo = dataPemilu("Gorontalo.csv", "KPU")
jambi = dataPemilu("Jambi.csv", "KPU")
jawaBarat = dataPemilu("JawaBarat.csv", "KPU")
jawaTengah = dataPemilu("JawaTengah.csv", "KPU")
jawaTimur = dataPemilu("JawaTimur.csv", "KPU")
kalimantanBarat = dataPemilu("KalimantanBarat.csv", "KPU")
kalimantanSelatan = dataPemilu("KalimantanSelatan.csv", "KPU")
kalimantanTengah = dataPemilu("KalimantanTengah.csv", "KPU")
kalimantanTimur = dataPemilu("KalimantanTimur.csv", "KPU")
kalimantanUtara = dataPemilu("KalimantanUtara.csv", "KPU")
kepulauanBangka = dataPemilu("KepulauanBangka.csv", "KPU")
kepulauanRiau = dataPemilu("KepulauanRiau.csv", "KPU")
lampung = dataPemilu("Lampung.csv", "KPU")
maluku = dataPemilu("Maluku.csv", "KPU")
malukuUtara = dataPemilu("MalukuUtara.csv", "KPU")
nusaTenggaraBarat = dataPemilu("NusaTenggaraBarat.csv", "KPU")
nusaTenggaraTimur = dataPemilu("NusaTenggaraTimur.csv", "KPU")
papua = dataPemilu("Papua.csv", "KPU")
papuaBarat = dataPemilu("PapuaBarat.csv", "KPU")
riau = dataPemilu("Riau.csv", "KPU")
sulawesiBarat = dataPemilu("SulawesiBarat.csv", "KPU")
sulawesiSelatan = dataPemilu("SulawesiSelatan.csv", "KPU")
sulawesiTengah = dataPemilu("SulawesiTengah.csv", "KPU")
sulawesiTenggara = dataPemilu("SulawesiTenggara.csv", "KPU")
sulawesiUtara = dataPemilu("SulawesiUtara.csv", "KPU")
sumateraBarat = dataPemilu("SumateraBarat.csv", "KPU")
sumateraSelatan = dataPemilu("SumateraSelatan.csv", "KPU")
sumateraUtara = dataPemilu("SumateraUtara.csv", "KPU")

sampleSize = 4000

aceh.randomSample(int(1.95/100*sampleSize))
bali.randomSample(int(1.53/100*sampleSize))
banten.randomSample(int(4.13/100*sampleSize))
bengkulu.randomSample(int(0.76/100*sampleSize))
daerahIstimewaYogyakarta.randomSample(int(1.46/100*sampleSize))
daerahKhususIbukotaJakarta.randomSample(int(3.58/100*sampleSize))
gorontalo.randomSample(int(0.42/100*sampleSize))
jambi.randomSample(int(1.40/100*sampleSize))
jawaBarat.randomSample(int(17.05/100*sampleSize))
jawaTengah.randomSample(int(14.25/100*sampleSize))
jawaTimur.randomSample(int(16.06/100*sampleSize))
kalimantanBarat.randomSample(int(2.04/100*sampleSize))
kalimantanSelatan.randomSample(int(1.34/100*sampleSize))
kalimantanTengah.randomSample(int(1.00/100*sampleSize))
kalimantanTimur.randomSample(int(1.34/100*sampleSize))
kalimantanUtara.randomSample(int(0.27/100*sampleSize))
kepulauanBangka.randomSample(int(0.47/100*sampleSize))
kepulauanRiau.randomSample(int(0.67/100*sampleSize))
lampung.randomSample(int(3.24/100*sampleSize))
maluku.randomSample(int(0.68/100*sampleSize))
malukuUtara.randomSample(int(0.47/100*sampleSize))
nusaTenggaraBarat.randomSample(int(1.98/100*sampleSize))
nusaTenggaraTimur.randomSample(int(1.85/100*sampleSize))
papua.randomSample(int(1.88/100*sampleSize))
papuaBarat.randomSample(int(0.48/100*sampleSize))
riau.randomSample(int(2.18/100*sampleSize))
sulawesiBarat.randomSample(int(0.48/100*sampleSize))
sulawesiSelatan.randomSample(int(3.25/100*sampleSize))
sulawesiTengah.randomSample(int(1.13/100*sampleSize))
sulawesiTenggara.randomSample(int(0.97/100*sampleSize))
sulawesiUtara.randomSample(int(0.97/100*sampleSize))
sumateraBarat.randomSample(int(2.06/100*sampleSize))
sumateraSelatan.randomSample(int(3.13/100*sampleSize))
sumateraUtara.randomSample(int(5.27/100*sampleSize))

nolSatuNasional = aceh.nolSatu + bali.nolSatu + banten.nolSatu + bengkulu.nolSatu + daerahIstimewaYogyakarta.nolSatu + daerahKhususIbukotaJakarta.nolSatu + gorontalo.nolSatu + jambi.nolSatu + jawaBarat.nolSatu + jawaTengah.nolSatu + jawaTimur.nolSatu + kalimantanBarat.nolSatu + kalimantanSelatan.nolSatu + kalimantanTengah.nolSatu + kalimantanTimur.nolSatu + kalimantanUtara.nolSatu + kepulauanBangka.nolSatu + kepulauanRiau.nolSatu + lampung.nolSatu + maluku.nolSatu + malukuUtara.nolSatu + nusaTenggaraBarat.nolSatu + nusaTenggaraTimur.nolSatu + papua.nolSatu + papuaBarat.nolSatu + riau.nolSatu + sulawesiBarat.nolSatu + sulawesiSelatan.nolSatu + sulawesiTengah.nolSatu + sulawesiTenggara.nolSatu + sulawesiUtara.nolSatu + sumateraBarat.nolSatu + sumateraSelatan.nolSatu + sumateraUtara.nolSatu
nolDuaNasional = aceh.nolDua + bali.nolDua + banten.nolDua + bengkulu.nolDua + daerahIstimewaYogyakarta.nolDua + daerahKhususIbukotaJakarta.nolDua + gorontalo.nolDua + jambi.nolDua + jawaBarat.nolDua + jawaTengah.nolDua + jawaTimur.nolDua + kalimantanBarat.nolDua + kalimantanSelatan.nolDua + kalimantanTengah.nolDua + kalimantanTimur.nolDua + kalimantanUtara.nolDua + kepulauanBangka.nolDua + kepulauanRiau.nolDua + lampung.nolDua + maluku.nolDua + malukuUtara.nolDua + nusaTenggaraBarat.nolDua + nusaTenggaraTimur.nolDua + papua.nolDua + papuaBarat.nolDua + riau.nolDua + sulawesiBarat.nolDua + sulawesiSelatan.nolDua + sulawesiTengah.nolDua + sulawesiTenggara.nolDua + sulawesiUtara.nolDua + sumateraBarat.nolDua + sumateraSelatan.nolDua + sumateraUtara.nolDua
totalSuaraNasional = aceh.totalSuara + bali.totalSuara + banten.totalSuara + bengkulu.totalSuara + daerahIstimewaYogyakarta.totalSuara + daerahKhususIbukotaJakarta.totalSuara + gorontalo.totalSuara + jambi.totalSuara + jawaBarat.totalSuara + jawaTengah.totalSuara + jawaTimur.totalSuara + kalimantanBarat.totalSuara + kalimantanSelatan.totalSuara + kalimantanTengah.totalSuara + kalimantanTimur.totalSuara + kalimantanUtara.totalSuara + kepulauanBangka.totalSuara + kepulauanRiau.totalSuara + lampung.totalSuara + maluku.totalSuara + malukuUtara.totalSuara + nusaTenggaraBarat.totalSuara + nusaTenggaraTimur.totalSuara + papua.totalSuara + papuaBarat.totalSuara + riau.totalSuara + sulawesiBarat.totalSuara + sulawesiSelatan.totalSuara + sulawesiTengah.totalSuara + sulawesiTenggara.totalSuara + sulawesiUtara.totalSuara + sumateraBarat.totalSuara + sumateraSelatan.totalSuara + sumateraUtara.totalSuara

persentaseNolSatuNasional = np.divide(nolSatuNasional, totalSuaraNasional)*100

sampleNolSatuNasional = aceh.sampleNolSatu + bali.sampleNolSatu + banten.sampleNolSatu + bengkulu.sampleNolSatu + daerahIstimewaYogyakarta.sampleNolSatu + daerahKhususIbukotaJakarta.sampleNolSatu + gorontalo.sampleNolSatu + jambi.sampleNolSatu + jawaBarat.sampleNolSatu + jawaTengah.sampleNolSatu + jawaTimur.sampleNolSatu + kalimantanBarat.sampleNolSatu + kalimantanSelatan.sampleNolSatu + kalimantanTengah.sampleNolSatu + kalimantanTimur.sampleNolSatu + kalimantanUtara.sampleNolSatu + kepulauanBangka.sampleNolSatu + kepulauanRiau.sampleNolSatu + lampung.sampleNolSatu + maluku.sampleNolSatu + malukuUtara.sampleNolSatu + nusaTenggaraBarat.sampleNolSatu + nusaTenggaraTimur.sampleNolSatu + papua.sampleNolSatu + papuaBarat.sampleNolSatu + riau.sampleNolSatu + sulawesiBarat.sampleNolSatu + sulawesiSelatan.sampleNolSatu + sulawesiTengah.sampleNolSatu + sulawesiTenggara.sampleNolSatu + sulawesiUtara.sampleNolSatu + sumateraBarat.sampleNolSatu + sumateraSelatan.sampleNolSatu + sumateraUtara.sampleNolSatu
sampleNolDuaNasional = aceh.sampleNolDua + bali.sampleNolDua + banten.sampleNolDua + bengkulu.sampleNolDua + daerahIstimewaYogyakarta.sampleNolDua + daerahKhususIbukotaJakarta.sampleNolDua + gorontalo.sampleNolDua + jambi.sampleNolDua + jawaBarat.sampleNolDua + jawaTengah.sampleNolDua + jawaTimur.sampleNolDua + kalimantanBarat.sampleNolDua + kalimantanSelatan.sampleNolDua + kalimantanTengah.sampleNolDua + kalimantanTimur.sampleNolDua + kalimantanUtara.sampleNolDua + kepulauanBangka.sampleNolDua + kepulauanRiau.sampleNolDua + lampung.sampleNolDua + maluku.sampleNolDua + malukuUtara.sampleNolDua + nusaTenggaraBarat.sampleNolDua + nusaTenggaraTimur.sampleNolDua + papua.sampleNolDua + papuaBarat.sampleNolDua + riau.sampleNolDua + sulawesiBarat.sampleNolDua + sulawesiSelatan.sampleNolDua + sulawesiTengah.sampleNolDua + sulawesiTenggara.sampleNolDua + sulawesiUtara.sampleNolDua + sumateraBarat.sampleNolDua + sumateraSelatan.sampleNolDua + sumateraUtara.sampleNolDua
sampleTotalSuaraNasional = aceh.sampleTotalSuara + bali.sampleTotalSuara + banten.sampleTotalSuara + bengkulu.sampleTotalSuara + daerahIstimewaYogyakarta.sampleTotalSuara + daerahKhususIbukotaJakarta.sampleTotalSuara + gorontalo.sampleTotalSuara + jambi.sampleTotalSuara + jawaBarat.sampleTotalSuara + jawaTengah.sampleTotalSuara + jawaTimur.sampleTotalSuara + kalimantanBarat.sampleTotalSuara + kalimantanSelatan.sampleTotalSuara + kalimantanTengah.sampleTotalSuara + kalimantanTimur.sampleTotalSuara + kalimantanUtara.sampleTotalSuara + kepulauanBangka.sampleTotalSuara + kepulauanRiau.sampleTotalSuara + lampung.sampleTotalSuara + maluku.sampleTotalSuara + malukuUtara.sampleTotalSuara + nusaTenggaraBarat.sampleTotalSuara + nusaTenggaraTimur.sampleTotalSuara + papua.sampleTotalSuara + papuaBarat.sampleTotalSuara + riau.sampleTotalSuara + sulawesiBarat.sampleTotalSuara + sulawesiSelatan.sampleTotalSuara + sulawesiTengah.sampleTotalSuara + sulawesiTenggara.sampleTotalSuara + sulawesiUtara.sampleTotalSuara + sumateraBarat.sampleTotalSuara + sumateraSelatan.sampleTotalSuara + sumateraUtara.sampleTotalSuara

persentaseSampleNolSatuNasional = np.divide(sampleNolSatuNasional, sampleTotalSuaraNasional)*100
persentaseSampleNolSatuNasionalSeries = pd.Series(persentaseSampleNolSatuNasional,
                                                      name = "Distribusi Persentase Suara 01 Stratified Random Sampling")

meanNolSatuNasional = np.sum(nolSatuNasional)/np.sum(totalSuaraNasional)*100
meanNolDuaNasional = 100 - meanNolSatuNasional

meanSampleNolSatuNasional = np.sum(sampleNolSatuNasional)/np.sum(sampleTotalSuaraNasional)*100
meanSampleNolDuaNasional = 100 - meanSampleNolSatuNasional
sampleStandardErrorOfMean = np.std(persentaseSampleNolSatuNasional)/np.sqrt(sampleSize)
marginErrorPercentage = sampleStandardErrorOfMean * 2.58

#sampleStandardErrorProportion = np.sqrt((meanSampleNolSatuNasional/100)*(meanNolDuaNasional/100)/sampleSize)
#marginErrorProportion = sampleStandardErrorProportion * 2.58
#marginErrorPercentage = marginErrorProportion * 100

plotDistribusiNasionalStratifiedRandomSample, ax = plt.subplots(2,1)
sns.distplot(persentaseNolSatuNasional, bins=100, ax = ax[0])
sns.distplot(persentaseSampleNolSatuNasionalSeries, bins=100, ax = ax[1])
plotDistribusiNasionalStratifiedRandomSample.savefig("StratifiedRandomSample.png")

plotDistribusiNasionalStratifiedRandomSample.suptitle('{:.2f}% vs {:.2f}% Real Count Sementara \n {:.2f}% vs {:.2f}% Stratified Random Sampling dengan MOE = +/-{:.2f}%'.format(meanNolSatuNasional, meanNolDuaNasional, meanSampleNolSatuNasional, meanSampleNolDuaNasional, marginErrorPercentage))