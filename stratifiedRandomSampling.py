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
    def __init__(self, filename, dataSource, totalTPS, sampleSize):
        self.totalTPS = totalTPS
        self.sampleSize = sampleSize
        self.nolSatu = []
        self.nolDua = []
        self.totalSuara = []
        self.sampleNolSatu = []
        self.sampleNolDua = []
        self.sampleTotalSuara = []
        self.nolSatuQuickCount = 0
        self.nolDuaQuickCount = 0
        self.totalSuaraQuickCount = 0
        self.varianceQuickCount = 0
        self.filename = filename
        self.getRawData(dataSource)
        self.cleanData()
        self.getQuickCountData()

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
    
    def randomSample(self):
        listSample = random.sample(range(len(self.totalSuara)), self.sampleSize)
        for x in listSample:
            self.sampleNolSatu.append(self.nolSatu[x])
            self.sampleNolDua.append(self.nolDua[x])
            self.sampleTotalSuara.append(self.totalSuara[x])
    
    def getQuickCountData(self):
        self.randomSample()
        self.nolSatuQuickCount = np.sum(self.sampleNolSatu)*self.totalTPS/self.sampleSize
        self.nolDuaQuickCount = np.sum(self.sampleNolDua)*self.totalTPS/self.sampleSize
        self.totalSuaraQuickCount = np.sum(self.sampleTotalSuara, dtype=np.float64)*self.totalTPS/self.sampleSize # needs 64 bit to prevent overflow

    def getVariance(self, proporsi):
        vhi = np.subtract(self.sampleNolSatu, np.multiply(proporsi, self.sampleTotalSuara))
        vh = np.sum(vhi)/self.sampleSize
        variance = np.sum(np.square(vhi-vh))/(self.sampleSize-1)
        varianceQuickCount = variance*self.totalTPS*(self.totalTPS-self.sampleSize)/self.sampleSize
        return varianceQuickCount

sampleSize = 2000

totalTPSAceh = 17389
totalTPSBali = 12386
totalTPSBanten = 33471
totalTPSBengkulu = 6165
totalTPSDaerahIstimewaYogyakarta = 11781
totalTPSDaerahKhususIbukotaJakarta = 29063
totalTPSGorontalo = 5866
totalTPSJambi = 11342
totalTPSJawaBarat = 70169
totalTPSJawaTengah = 86121
totalTPSJawaTimur = 67454
totalTPSKalimantanBarat = 10791
totalTPSKalimantanSelatan = 6722
totalTPSKalimantanTengah = 4780
totalTPSKalimantanTimur = 6780
totalTPSKalimantanUtara = 1512
totalTPSKepulauanBangka = 3597
totalTPSKepulauanRiau = 4659
totalTPSLampung = 20407
totalTPSMaluku = 2705
totalTPSMalukuUtara = 3805
totalTPSNusaTenggaraBarat = 10082
totalTPSNusaTenggaraTimur = 7656
totalTPSPapua = 1006
totalTPSPapuaBarat = 749
totalTPSRiau = 13174
totalTPSSulawesiBarat = 1857
totalTPSSulawesiSelatan = 14608
totalTPSSulawesiTengah = 3719
totalTPSSulawesiTenggara = 3710
totalTPSSulawesiUtara = 3986
totalTPSSumateraBarat = 13804
totalTPSSumateraSelatan = 19427
totalTPSSumateraUtara = 30883
totalTPSNasional = 809497

aceh = dataPemilu("Aceh.csv", "KPU", totalTPSAceh, int(1.95/100*sampleSize))
bali = dataPemilu("Bali.csv", "KPU", totalTPSBali, int(1.53/100*sampleSize))
banten = dataPemilu("Banten.csv", "KPU", totalTPSBanten, int(4.13/100*sampleSize))
bengkulu = dataPemilu("Bengkulu.csv", "KPU", totalTPSBengkulu, int(0.76/100*sampleSize))
daerahIstimewaYogyakarta = dataPemilu("DaerahIstimewaYogyakarta.csv", "KPU", totalTPSDaerahIstimewaYogyakarta, int(1.46/100*sampleSize))
daerahKhususIbukotaJakarta = dataPemilu("DaerahKhususIbukotaJakarta.csv", "KPU", totalTPSDaerahKhususIbukotaJakarta, int(3.58/100*sampleSize))
gorontalo = dataPemilu("Gorontalo.csv", "KPU", totalTPSGorontalo, int(0.42/100*sampleSize))
jambi = dataPemilu("Jambi.csv", "KPU", totalTPSJambi, int(1.40/100*sampleSize))
jawaBarat = dataPemilu("JawaBarat.csv", "KPU", totalTPSJawaBarat, int(17.05/100*sampleSize))
jawaTengah = dataPemilu("JawaTengah.csv", "KPU", totalTPSJawaTengah, int(14.25/100*sampleSize))
jawaTimur = dataPemilu("JawaTimur.csv", "KPU", totalTPSJawaTimur, int(16.06/100*sampleSize))
kalimantanBarat = dataPemilu("KalimantanBarat.csv", "KPU", totalTPSKalimantanBarat, int(2.04/100*sampleSize))
kalimantanSelatan = dataPemilu("KalimantanSelatan.csv", "KPU", totalTPSKalimantanSelatan, int(1.34/100*sampleSize))
kalimantanTengah = dataPemilu("KalimantanTengah.csv", "KPU", totalTPSKalimantanTengah, int(1.00/100*sampleSize))
kalimantanTimur = dataPemilu("KalimantanTimur.csv", "KPU", totalTPSKalimantanTimur, int(1.34/100*sampleSize))
kalimantanUtara = dataPemilu("KalimantanUtara.csv", "KPU", totalTPSKalimantanUtara, int(0.27/100*sampleSize))
kepulauanBangka = dataPemilu("KepulauanBangka.csv", "KPU", totalTPSKepulauanBangka, int(0.47/100*sampleSize))
kepulauanRiau = dataPemilu("KepulauanRiau.csv", "KPU", totalTPSKepulauanRiau, int(0.67/100*sampleSize))
lampung = dataPemilu("Lampung.csv", "KPU", totalTPSLampung, int(3.24/100*sampleSize))
maluku = dataPemilu("Maluku.csv", "KPU", totalTPSMaluku, int(0.68/100*sampleSize))
malukuUtara = dataPemilu("MalukuUtara.csv", "KPU", totalTPSMalukuUtara, int(0.47/100*sampleSize))
nusaTenggaraBarat = dataPemilu("NusaTenggaraBarat.csv", "KPU", totalTPSNusaTenggaraBarat, int(1.98/100*sampleSize))
nusaTenggaraTimur = dataPemilu("NusaTenggaraTimur.csv", "KPU", totalTPSNusaTenggaraTimur, int(1.85/100*sampleSize))
papua = dataPemilu("Papua.csv", "KPU", totalTPSPapua, int(1.88/100*sampleSize))
papuaBarat = dataPemilu("PapuaBarat.csv", "KPU", totalTPSPapuaBarat, int(0.48/100*sampleSize))
riau = dataPemilu("Riau.csv", "KPU", totalTPSRiau, int(2.18/100*sampleSize))
sulawesiBarat = dataPemilu("SulawesiBarat.csv", "KPU", totalTPSSulawesiBarat, int(0.48/100*sampleSize))
sulawesiSelatan = dataPemilu("SulawesiSelatan.csv", "KPU", totalTPSSulawesiSelatan, int(3.25/100*sampleSize))
sulawesiTengah = dataPemilu("SulawesiTengah.csv", "KPU", totalTPSSulawesiTengah, int(1.13/100*sampleSize))
sulawesiTenggara = dataPemilu("SulawesiTenggara.csv", "KPU", totalTPSSulawesiTenggara, int(0.97/100*sampleSize))
sulawesiUtara = dataPemilu("SulawesiUtara.csv", "KPU", totalTPSSulawesiUtara, int(0.97/100*sampleSize))
sumateraBarat = dataPemilu("SumateraBarat.csv", "KPU", totalTPSSumateraBarat, int(2.06/100*sampleSize))
sumateraSelatan = dataPemilu("SumateraSelatan.csv", "KPU", totalTPSSumateraSelatan, int(3.13/100*sampleSize))
sumateraUtara = dataPemilu("SumateraUtara.csv", "KPU", totalTPSSumateraUtara, int(5.27/100*sampleSize))

## Real Count KPU

nolSatuNasional = aceh.nolSatu + bali.nolSatu + banten.nolSatu + bengkulu.nolSatu + daerahIstimewaYogyakarta.nolSatu + daerahKhususIbukotaJakarta.nolSatu + gorontalo.nolSatu + jambi.nolSatu + jawaBarat.nolSatu + jawaTengah.nolSatu + jawaTimur.nolSatu + kalimantanBarat.nolSatu + kalimantanSelatan.nolSatu + kalimantanTengah.nolSatu + kalimantanTimur.nolSatu + kalimantanUtara.nolSatu + kepulauanBangka.nolSatu + kepulauanRiau.nolSatu + lampung.nolSatu + maluku.nolSatu + malukuUtara.nolSatu + nusaTenggaraBarat.nolSatu + nusaTenggaraTimur.nolSatu + papua.nolSatu + papuaBarat.nolSatu + riau.nolSatu + sulawesiBarat.nolSatu + sulawesiSelatan.nolSatu + sulawesiTengah.nolSatu + sulawesiTenggara.nolSatu + sulawesiUtara.nolSatu + sumateraBarat.nolSatu + sumateraSelatan.nolSatu + sumateraUtara.nolSatu
nolDuaNasional = aceh.nolDua + bali.nolDua + banten.nolDua + bengkulu.nolDua + daerahIstimewaYogyakarta.nolDua + daerahKhususIbukotaJakarta.nolDua + gorontalo.nolDua + jambi.nolDua + jawaBarat.nolDua + jawaTengah.nolDua + jawaTimur.nolDua + kalimantanBarat.nolDua + kalimantanSelatan.nolDua + kalimantanTengah.nolDua + kalimantanTimur.nolDua + kalimantanUtara.nolDua + kepulauanBangka.nolDua + kepulauanRiau.nolDua + lampung.nolDua + maluku.nolDua + malukuUtara.nolDua + nusaTenggaraBarat.nolDua + nusaTenggaraTimur.nolDua + papua.nolDua + papuaBarat.nolDua + riau.nolDua + sulawesiBarat.nolDua + sulawesiSelatan.nolDua + sulawesiTengah.nolDua + sulawesiTenggara.nolDua + sulawesiUtara.nolDua + sumateraBarat.nolDua + sumateraSelatan.nolDua + sumateraUtara.nolDua
totalSuaraNasional = aceh.totalSuara + bali.totalSuara + banten.totalSuara + bengkulu.totalSuara + daerahIstimewaYogyakarta.totalSuara + daerahKhususIbukotaJakarta.totalSuara + gorontalo.totalSuara + jambi.totalSuara + jawaBarat.totalSuara + jawaTengah.totalSuara + jawaTimur.totalSuara + kalimantanBarat.totalSuara + kalimantanSelatan.totalSuara + kalimantanTengah.totalSuara + kalimantanTimur.totalSuara + kalimantanUtara.totalSuara + kepulauanBangka.totalSuara + kepulauanRiau.totalSuara + lampung.totalSuara + maluku.totalSuara + malukuUtara.totalSuara + nusaTenggaraBarat.totalSuara + nusaTenggaraTimur.totalSuara + papua.totalSuara + papuaBarat.totalSuara + riau.totalSuara + sulawesiBarat.totalSuara + sulawesiSelatan.totalSuara + sulawesiTengah.totalSuara + sulawesiTenggara.totalSuara + sulawesiUtara.totalSuara + sumateraBarat.totalSuara + sumateraSelatan.totalSuara + sumateraUtara.totalSuara

persentaseNolSatuNasional = np.divide(nolSatuNasional, totalSuaraNasional)*100

meanNolSatuNasional = np.sum(nolSatuNasional)/np.sum(totalSuaraNasional)*100
meanNolDuaNasional = 100 - meanNolSatuNasional

## Stratified Random Sampling

nolSatuQuickCountNasional = aceh.nolSatuQuickCount + bali.nolSatuQuickCount + banten.nolSatuQuickCount + bengkulu.nolSatuQuickCount + daerahIstimewaYogyakarta.nolSatuQuickCount + daerahKhususIbukotaJakarta.nolSatuQuickCount + gorontalo.nolSatuQuickCount + jambi.nolSatuQuickCount + jawaBarat.nolSatuQuickCount + jawaTengah.nolSatuQuickCount + jawaTimur.nolSatuQuickCount + kalimantanBarat.nolSatuQuickCount + kalimantanSelatan.nolSatuQuickCount + kalimantanTengah.nolSatuQuickCount + kalimantanTimur.nolSatuQuickCount + kalimantanUtara.nolSatuQuickCount + kepulauanBangka.nolSatuQuickCount + kepulauanRiau.nolSatuQuickCount + lampung.nolSatuQuickCount + maluku.nolSatuQuickCount + malukuUtara.nolSatuQuickCount + nusaTenggaraBarat.nolSatuQuickCount + nusaTenggaraTimur.nolSatuQuickCount + papua.nolSatuQuickCount + papuaBarat.nolSatuQuickCount + riau.nolSatuQuickCount + sulawesiBarat.nolSatuQuickCount + sulawesiSelatan.nolSatuQuickCount + sulawesiTengah.nolSatuQuickCount + sulawesiTenggara.nolSatuQuickCount + sulawesiUtara.nolSatuQuickCount + sumateraBarat.nolSatuQuickCount + sumateraSelatan.nolSatuQuickCount + sumateraUtara.nolSatuQuickCount
nolDuaQuickCountNasional = aceh.nolDuaQuickCount + bali.nolDuaQuickCount + banten.nolDuaQuickCount + bengkulu.nolDuaQuickCount + daerahIstimewaYogyakarta.nolDuaQuickCount + daerahKhususIbukotaJakarta.nolDuaQuickCount + gorontalo.nolDuaQuickCount + jambi.nolDuaQuickCount + jawaBarat.nolDuaQuickCount + jawaTengah.nolDuaQuickCount + jawaTimur.nolDuaQuickCount + kalimantanBarat.nolDuaQuickCount + kalimantanSelatan.nolDuaQuickCount + kalimantanTengah.nolDuaQuickCount + kalimantanTimur.nolDuaQuickCount + kalimantanUtara.nolDuaQuickCount + kepulauanBangka.nolDuaQuickCount + kepulauanRiau.nolDuaQuickCount + lampung.nolDuaQuickCount + maluku.nolDuaQuickCount + malukuUtara.nolDuaQuickCount + nusaTenggaraBarat.nolDuaQuickCount + nusaTenggaraTimur.nolDuaQuickCount + papua.nolDuaQuickCount + papuaBarat.nolDuaQuickCount + riau.nolDuaQuickCount + sulawesiBarat.nolDuaQuickCount + sulawesiSelatan.nolDuaQuickCount + sulawesiTengah.nolDuaQuickCount + sulawesiTenggara.nolDuaQuickCount + sulawesiUtara.nolDuaQuickCount + sumateraBarat.nolDuaQuickCount + sumateraSelatan.nolDuaQuickCount + sumateraUtara.nolDuaQuickCount
totalSuaraQuickCountNasional = aceh.totalSuaraQuickCount + bali.totalSuaraQuickCount + banten.totalSuaraQuickCount + bengkulu.totalSuaraQuickCount + daerahIstimewaYogyakarta.totalSuaraQuickCount + daerahKhususIbukotaJakarta.totalSuaraQuickCount + gorontalo.totalSuaraQuickCount + jambi.totalSuaraQuickCount + jawaBarat.totalSuaraQuickCount + jawaTengah.totalSuaraQuickCount + jawaTimur.totalSuaraQuickCount + kalimantanBarat.totalSuaraQuickCount + kalimantanSelatan.totalSuaraQuickCount + kalimantanTengah.totalSuaraQuickCount + kalimantanTimur.totalSuaraQuickCount + kalimantanUtara.totalSuaraQuickCount + kepulauanBangka.totalSuaraQuickCount + kepulauanRiau.totalSuaraQuickCount + lampung.totalSuaraQuickCount + maluku.totalSuaraQuickCount + malukuUtara.totalSuaraQuickCount + nusaTenggaraBarat.totalSuaraQuickCount + nusaTenggaraTimur.totalSuaraQuickCount + papua.totalSuaraQuickCount + papuaBarat.totalSuaraQuickCount + riau.totalSuaraQuickCount + sulawesiBarat.totalSuaraQuickCount + sulawesiSelatan.totalSuaraQuickCount + sulawesiTengah.totalSuaraQuickCount + sulawesiTenggara.totalSuaraQuickCount + sulawesiUtara.totalSuaraQuickCount + sumateraBarat.totalSuaraQuickCount + sumateraSelatan.totalSuaraQuickCount + sumateraUtara.totalSuaraQuickCount

proporsiNolSatu = nolSatuQuickCountNasional/totalSuaraQuickCountNasional
proporsiNolDua = nolDuaQuickCountNasional/totalSuaraQuickCountNasional
persentaseNolSatu = proporsiNolSatu*100
persentaseNolDua = proporsiNolDua*100

print(proporsiNolSatu)
print(proporsiNolDua)

varianceNasional = aceh.getVariance(proporsiNolSatu) + bali.getVariance(proporsiNolSatu) + banten.getVariance(proporsiNolSatu) + bengkulu.getVariance(proporsiNolSatu) + daerahIstimewaYogyakarta.getVariance(proporsiNolSatu) + daerahKhususIbukotaJakarta.getVariance(proporsiNolSatu) + gorontalo.getVariance(proporsiNolSatu) + jambi.getVariance(proporsiNolSatu) + jawaBarat.getVariance(proporsiNolSatu) + jawaTengah.getVariance(proporsiNolSatu) + jawaTimur.getVariance(proporsiNolSatu) + kalimantanBarat.getVariance(proporsiNolSatu) + kalimantanSelatan.getVariance(proporsiNolSatu) + kalimantanTengah.getVariance(proporsiNolSatu) + kalimantanTimur.getVariance(proporsiNolSatu) + kalimantanUtara.getVariance(proporsiNolSatu) + kepulauanBangka.getVariance(proporsiNolSatu) + kepulauanRiau.getVariance(proporsiNolSatu) + lampung.getVariance(proporsiNolSatu) + maluku.getVariance(proporsiNolSatu) + malukuUtara.getVariance(proporsiNolSatu) + nusaTenggaraBarat.getVariance(proporsiNolSatu) + nusaTenggaraTimur.getVariance(proporsiNolSatu) + papua.getVariance(proporsiNolSatu) + papuaBarat.getVariance(proporsiNolSatu) + riau.getVariance(proporsiNolSatu) + sulawesiBarat.getVariance(proporsiNolSatu) + sulawesiSelatan.getVariance(proporsiNolSatu) + sulawesiTengah.getVariance(proporsiNolSatu) + sulawesiTenggara.getVariance(proporsiNolSatu) + sulawesiUtara.getVariance(proporsiNolSatu) + sumateraBarat.getVariance(proporsiNolSatu) + sumateraSelatan.getVariance(proporsiNolSatu) + sumateraUtara.getVariance(proporsiNolSatu)

standardErrorProporsi = np.sqrt(1/np.square(totalSuaraQuickCountNasional)*varianceNasional)
marginOfErrorProporsi = 2*standardErrorProporsi
marginOfErrorPercentage = marginOfErrorProporsi*100

sampleNolSatuNasional = aceh.sampleNolSatu + bali.sampleNolSatu + banten.sampleNolSatu + bengkulu.sampleNolSatu + daerahIstimewaYogyakarta.sampleNolSatu + daerahKhususIbukotaJakarta.sampleNolSatu + gorontalo.sampleNolSatu + jambi.sampleNolSatu + jawaBarat.sampleNolSatu + jawaTengah.sampleNolSatu + jawaTimur.sampleNolSatu + kalimantanBarat.sampleNolSatu + kalimantanSelatan.sampleNolSatu + kalimantanTengah.sampleNolSatu + kalimantanTimur.sampleNolSatu + kalimantanUtara.sampleNolSatu + kepulauanBangka.sampleNolSatu + kepulauanRiau.sampleNolSatu + lampung.sampleNolSatu + maluku.sampleNolSatu + malukuUtara.sampleNolSatu + nusaTenggaraBarat.sampleNolSatu + nusaTenggaraTimur.sampleNolSatu + papua.sampleNolSatu + papuaBarat.sampleNolSatu + riau.sampleNolSatu + sulawesiBarat.sampleNolSatu + sulawesiSelatan.sampleNolSatu + sulawesiTengah.sampleNolSatu + sulawesiTenggara.sampleNolSatu + sulawesiUtara.sampleNolSatu + sumateraBarat.sampleNolSatu + sumateraSelatan.sampleNolSatu + sumateraUtara.sampleNolSatu
sampleNolDuaNasional = aceh.sampleNolDua + bali.sampleNolDua + banten.sampleNolDua + bengkulu.sampleNolDua + daerahIstimewaYogyakarta.sampleNolDua + daerahKhususIbukotaJakarta.sampleNolDua + gorontalo.sampleNolDua + jambi.sampleNolDua + jawaBarat.sampleNolDua + jawaTengah.sampleNolDua + jawaTimur.sampleNolDua + kalimantanBarat.sampleNolDua + kalimantanSelatan.sampleNolDua + kalimantanTengah.sampleNolDua + kalimantanTimur.sampleNolDua + kalimantanUtara.sampleNolDua + kepulauanBangka.sampleNolDua + kepulauanRiau.sampleNolDua + lampung.sampleNolDua + maluku.sampleNolDua + malukuUtara.sampleNolDua + nusaTenggaraBarat.sampleNolDua + nusaTenggaraTimur.sampleNolDua + papua.sampleNolDua + papuaBarat.sampleNolDua + riau.sampleNolDua + sulawesiBarat.sampleNolDua + sulawesiSelatan.sampleNolDua + sulawesiTengah.sampleNolDua + sulawesiTenggara.sampleNolDua + sulawesiUtara.sampleNolDua + sumateraBarat.sampleNolDua + sumateraSelatan.sampleNolDua + sumateraUtara.sampleNolDua
sampleTotalSuaraNasional = aceh.sampleTotalSuara + bali.sampleTotalSuara + banten.sampleTotalSuara + bengkulu.sampleTotalSuara + daerahIstimewaYogyakarta.sampleTotalSuara + daerahKhususIbukotaJakarta.sampleTotalSuara + gorontalo.sampleTotalSuara + jambi.sampleTotalSuara + jawaBarat.sampleTotalSuara + jawaTengah.sampleTotalSuara + jawaTimur.sampleTotalSuara + kalimantanBarat.sampleTotalSuara + kalimantanSelatan.sampleTotalSuara + kalimantanTengah.sampleTotalSuara + kalimantanTimur.sampleTotalSuara + kalimantanUtara.sampleTotalSuara + kepulauanBangka.sampleTotalSuara + kepulauanRiau.sampleTotalSuara + lampung.sampleTotalSuara + maluku.sampleTotalSuara + malukuUtara.sampleTotalSuara + nusaTenggaraBarat.sampleTotalSuara + nusaTenggaraTimur.sampleTotalSuara + papua.sampleTotalSuara + papuaBarat.sampleTotalSuara + riau.sampleTotalSuara + sulawesiBarat.sampleTotalSuara + sulawesiSelatan.sampleTotalSuara + sulawesiTengah.sampleTotalSuara + sulawesiTenggara.sampleTotalSuara + sulawesiUtara.sampleTotalSuara + sumateraBarat.sampleTotalSuara + sumateraSelatan.sampleTotalSuara + sumateraUtara.sampleTotalSuara

persentaseSampleNolSatuNasional = np.divide(sampleNolSatuNasional, sampleTotalSuaraNasional)*100
persentaseSampleNolSatuNasionalSeries = pd.Series(persentaseSampleNolSatuNasional,
                                                      name = "Distribusi Persentase Suara 01 Stratified Random Sampling")

plotDistribusiNasionalStratifiedRandomSample, ax = plt.subplots(2,1)
sns.distplot(persentaseNolSatuNasional, kde=False, bins=100, ax = ax[0])
sns.distplot(persentaseSampleNolSatuNasionalSeries, kde=False, bins=100, ax = ax[1])
plotDistribusiNasionalStratifiedRandomSample.suptitle('{:.2f}% vs {:.2f}% Real Count Sementara \n {:.2f}% vs {:.2f}% Stratified Random Sampling dengan MOE = +/-{:.2f}%'.format(meanNolSatuNasional, meanNolDuaNasional, persentaseNolSatu, persentaseNolDua, marginOfErrorPercentage))

plotDistribusiNasionalStratifiedRandomSample.savefig("StratifiedRandomSample4.png")