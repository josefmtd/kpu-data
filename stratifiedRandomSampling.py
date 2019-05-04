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

nolSatuNasional = aceh.nolSatu + bali.nolSatu + banten.nolSatu + bengkulu.nolSatu + daerahIstimewaYogyakarta.nolSatu + daerahKhususIbukotaJakarta.nolSatu + gorontalo.nolSatu + jambi.nolSatu + jawaBarat.nolSatu + jawaTengah.nolSatu + jawaTimur.nolSatu + kalimantanBarat.nolSatu + kalimantanSelatan.nolSatu + kalimantanTengah.nolSatu + kalimantanTimur.nolSatu + kalimantanUtara.nolSatu + kepulauanBangka.nolSatu + kepulauanRiau.nolSatu + lampung.nolSatu + maluku.nolSatu + malukuUtara.nolSatu + nusaTenggaraBarat.nolSatu + nusaTenggaraTimur.nolSatu + papua.nolSatu + papuaBarat.nolSatu + riau.nolSatu + sulawesiBarat.nolSatu + sulawesiSelatan.nolSatu + sulawesiTengah.nolSatu + sulawesiTenggara.nolSatu + sulawesiUtara.nolSatu + sumateraBarat.nolSatu + sumateraSelatan.nolSatu + sumateraUtara.nolSatu
nolDuaNasional = aceh.nolDua + bali.nolDua + banten.nolDua + bengkulu.nolDua + daerahIstimewaYogyakarta.nolDua + daerahKhususIbukotaJakarta.nolDua + gorontalo.nolDua + jambi.nolDua + jawaBarat.nolDua + jawaTengah.nolDua + jawaTimur.nolDua + kalimantanBarat.nolDua + kalimantanSelatan.nolDua + kalimantanTengah.nolDua + kalimantanTimur.nolDua + kalimantanUtara.nolDua + kepulauanBangka.nolDua + kepulauanRiau.nolDua + lampung.nolDua + maluku.nolDua + malukuUtara.nolDua + nusaTenggaraBarat.nolDua + nusaTenggaraTimur.nolDua + papua.nolDua + papuaBarat.nolDua + riau.nolDua + sulawesiBarat.nolDua + sulawesiSelatan.nolDua + sulawesiTengah.nolDua + sulawesiTenggara.nolDua + sulawesiUtara.nolDua + sumateraBarat.nolDua + sumateraSelatan.nolDua + sumateraUtara.nolDua
totalSuaraNasional = aceh.totalSuara + bali.totalSuara + banten.totalSuara + bengkulu.totalSuara + daerahIstimewaYogyakarta.totalSuara + daerahKhususIbukotaJakarta.totalSuara + gorontalo.totalSuara + jambi.totalSuara + jawaBarat.totalSuara + jawaTengah.totalSuara + jawaTimur.totalSuara + kalimantanBarat.totalSuara + kalimantanSelatan.totalSuara + kalimantanTengah.totalSuara + kalimantanTimur.totalSuara + kalimantanUtara.totalSuara + kepulauanBangka.totalSuara + kepulauanRiau.totalSuara + lampung.totalSuara + maluku.totalSuara + malukuUtara.totalSuara + nusaTenggaraBarat.totalSuara + nusaTenggaraTimur.totalSuara + papua.totalSuara + papuaBarat.totalSuara + riau.totalSuara + sulawesiBarat.totalSuara + sulawesiSelatan.totalSuara + sulawesiTengah.totalSuara + sulawesiTenggara.totalSuara + sulawesiUtara.totalSuara + sumateraBarat.totalSuara + sumateraSelatan.totalSuara + sumateraUtara.totalSuara

persentaseNolSatuNasional = np.divide(nolSatuNasional, totalSuaraNasional)*100
persentaseNolSatuNasionalSeries = pd.Series(persentaseNolSatuNasional,
                                        name = "Distribusi Persentase Suara 01 Nasional")

plotDistribusiNasional, seabornNasional = plt.subplots()
sns.distplot(persentaseNolSatuNasionalSeries, kde=False, bins=100, ax = seabornNasional)
plotDistribusiNasional.savefig("Nasional.png")
