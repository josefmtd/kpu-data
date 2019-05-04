# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:35:56 2019

@author: JosefStevanus
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

acehData = pd.read_csv("Aceh.csv")

nolSatuAceh = acehData["01 KPU"]
nolDuaAceh = acehData["02 KPU"]

cleanNolSatuAceh = []
cleanNolDuaAceh = []

for x in range(len(nolSatuAceh)):
    if nolSatuAceh[x] == 0 and nolDuaAceh[x] == 0:
        continue
    else:
        cleanNolSatuAceh.append(nolSatuAceh[x])
        cleanNolDuaAceh.append(nolDuaAceh[x])
        
cleanTotalSuaraAceh = np.add(cleanNolSatuAceh, cleanNolDuaAceh)

percentageNolSatuAceh = np.divide(cleanNolSatuAceh, cleanTotalSuaraAceh)*100
percentageNolSatuAcehSeries = pd.Series(percentageNolSatuAceh,
                                        name = "Distribusi Persentase Suara 01 di Aceh")

plotDistribusiAceh, seabornAceh = plt.subplots()
sns.distplot(percentageNolSatuAcehSeries, kde=False, bins=100, ax=seabornAceh)
plotDistribusiAceh.savefig("Aceh.png")

baliData = pd.read_csv("Bali.csv")

nolSatuBali = baliData["01 KPU"]
nolDuaBali = baliData["02 KPU"]

cleanNolSatuBali = []
cleanNolDuaBali = []

for x in range(len(nolSatuBali)):
    if nolSatuBali[x] == 0 and nolDuaBali[x] == 0:
        continue
    else:
        cleanNolSatuBali.append(nolSatuBali[x])
        cleanNolDuaBali.append(nolDuaBali[x])
        
cleanTotalSuaraBali = np.add(cleanNolSatuBali, cleanNolDuaBali)

percentageNolSatuBali = np.divide(cleanNolSatuBali, cleanTotalSuaraBali)*100
percentageNolSatuBaliSeries = pd.Series(percentageNolSatuBali,
                                        name = "Distribusi Persentase Suara 01 di Bali")

plotDistribusiBali, seabornBali = plt.subplots()
sns.distplot(percentageNolSatuBaliSeries, kde=False, bins=100, ax=seabornBali)
plotDistribusiBali.savefig("Bali.png")

bantenData = pd.read_csv("Banten.csv")

nolSatuBanten = bantenData["01 KPU"]
nolDuaBanten = bantenData["02 KPU"]

cleanNolSatuBanten = []
cleanNolDuaBanten = []

for x in range(len(nolSatuBanten)):
    if nolSatuBanten[x] == 0 and nolDuaBanten[x] == 0:
        continue
    else:
        cleanNolSatuBanten.append(nolSatuBanten[x])
        cleanNolDuaBanten.append(nolDuaBanten[x])
        
cleanTotalSuaraBanten = np.add(cleanNolSatuBanten, cleanNolDuaBanten)

percentageNolSatuBanten = np.divide(cleanNolSatuBanten, cleanTotalSuaraBanten)*100
percentageNolSatuBantenSeries = pd.Series(percentageNolSatuBanten,
                                        name = "Distribusi Persentase Suara 01 di Banten")

plotDistribusiBanten, seabornBanten = plt.subplots()
sns.distplot(percentageNolSatuBantenSeries, kde=False, bins=100, ax=seabornBanten)
plotDistribusiBanten.savefig("Banten.png")

bengkuluData = pd.read_csv("Bengkulu.csv")

nolSatuBengkulu = bengkuluData["01 KPU"]
nolDuaBengkulu = bengkuluData["02 KPU"]

cleanNolSatuBengkulu = []
cleanNolDuaBengkulu = []

for x in range(len(nolSatuBengkulu)):
    if nolSatuBengkulu[x] == 0 and nolDuaBengkulu[x] == 0:
        continue
    else:
        cleanNolSatuBengkulu.append(nolSatuBengkulu[x])
        cleanNolDuaBengkulu.append(nolDuaBengkulu[x])
        
cleanTotalSuaraBengkulu = np.add(cleanNolSatuBengkulu, cleanNolDuaBengkulu)

percentageNolSatuBengkulu = np.divide(cleanNolSatuBengkulu, cleanTotalSuaraBengkulu)*100
percentageNolSatuBengkuluSeries = pd.Series(percentageNolSatuBengkulu,
                                        name = "Distribusi Persentase Suara 01 di Bengkulu")

plotDistribusiBengkulu, seabornBengkulu = plt.subplots()
sns.distplot(percentageNolSatuBengkuluSeries, kde=False, bins=100, ax=seabornBengkulu)
plotDistribusiBengkulu.savefig("Bengkulu.png")

daerahIstimewaYogyakartaData = pd.read_csv("DaerahIstimewaYogyakarta.csv")

nolSatuDaerahIstimewaYogyakarta = daerahIstimewaYogyakartaData["01 KPU"]
nolDuaDaerahIstimewaYogyakarta = daerahIstimewaYogyakartaData["02 KPU"]

cleanNolSatuDaerahIstimewaYogyakarta = []
cleanNolDuaDaerahIstimewaYogyakarta = []

for x in range(len(nolSatuDaerahIstimewaYogyakarta)):
    if nolSatuDaerahIstimewaYogyakarta[x] == 0 and nolDuaDaerahIstimewaYogyakarta[x] == 0:
        continue
    else:
        cleanNolSatuDaerahIstimewaYogyakarta.append(nolSatuDaerahIstimewaYogyakarta[x])
        cleanNolDuaDaerahIstimewaYogyakarta.append(nolDuaDaerahIstimewaYogyakarta[x])
        
cleanTotalSuaraDaerahIstimewaYogyakarta = np.add(cleanNolSatuDaerahIstimewaYogyakarta, cleanNolDuaDaerahIstimewaYogyakarta)

percentageNolSatuDaerahIstimewaYogyakarta = np.divide(cleanNolSatuDaerahIstimewaYogyakarta, cleanTotalSuaraDaerahIstimewaYogyakarta)*100
percentageNolSatuDaerahIstimewaYogyakartaSeries = pd.Series(percentageNolSatuDaerahIstimewaYogyakarta,
                                        name = "Distribusi Persentase Suara 01 di DaerahIstimewaYogyakarta")

plotDistribusiDaerahIstimewaYogyakarta, seabornDaerahIstimewaYogyakarta = plt.subplots()
sns.distplot(percentageNolSatuDaerahIstimewaYogyakartaSeries, kde=False, bins=100, ax=seabornDaerahIstimewaYogyakarta)
plotDistribusiDaerahIstimewaYogyakarta.savefig("DaerahIstimewaYogyakarta.png")

daerahKhususIbukotaJakartaData = pd.read_csv("DaerahKhususIbukotaJakarta.csv")

nolSatuDaerahKhususIbukotaJakarta = daerahKhususIbukotaJakartaData["01 KPU"]
nolDuaDaerahKhususIbukotaJakarta = daerahKhususIbukotaJakartaData["02 KPU"]

cleanNolSatuDaerahKhususIbukotaJakarta = []
cleanNolDuaDaerahKhususIbukotaJakarta = []

for x in range(len(nolSatuDaerahKhususIbukotaJakarta)):
    if nolSatuDaerahKhususIbukotaJakarta[x] == 0 and nolDuaDaerahKhususIbukotaJakarta[x] == 0:
        continue
    else:
        cleanNolSatuDaerahKhususIbukotaJakarta.append(nolSatuDaerahKhususIbukotaJakarta[x])
        cleanNolDuaDaerahKhususIbukotaJakarta.append(nolDuaDaerahKhususIbukotaJakarta[x])
        
cleanTotalSuaraDaerahKhususIbukotaJakarta = np.add(cleanNolSatuDaerahKhususIbukotaJakarta, cleanNolDuaDaerahKhususIbukotaJakarta)

percentageNolSatuDaerahKhususIbukotaJakarta = np.divide(cleanNolSatuDaerahKhususIbukotaJakarta, cleanTotalSuaraDaerahKhususIbukotaJakarta)*100
percentageNolSatuDaerahKhususIbukotaJakartaSeries = pd.Series(percentageNolSatuDaerahKhususIbukotaJakarta,
                                        name = "Distribusi Persentase Suara 01 di DaerahKhususIbukotaJakarta")

plotDistribusiDaerahKhususIbukotaJakarta, seabornDaerahKhususIbukotaJakarta = plt.subplots()
sns.distplot(percentageNolSatuDaerahKhususIbukotaJakartaSeries, kde=False, bins=100, ax = seabornDaerahKhususIbukotaJakarta)
plotDistribusiDaerahKhususIbukotaJakarta.savefig("DaerahKhususIbukotaJakarta.png")

gorontaloData = pd.read_csv("Gorontalo.csv")

nolSatuGorontalo = gorontaloData["01 KPU"]
nolDuaGorontalo = gorontaloData["02 KPU"]

cleanNolSatuGorontalo = []
cleanNolDuaGorontalo = []

for x in range(len(nolSatuGorontalo)):
    if nolSatuGorontalo[x] == 0 and nolDuaGorontalo[x] == 0:
        continue
    else:
        cleanNolSatuGorontalo.append(nolSatuGorontalo[x])
        cleanNolDuaGorontalo.append(nolDuaGorontalo[x])
        
cleanTotalSuaraGorontalo = np.add(cleanNolSatuGorontalo, cleanNolDuaGorontalo)

percentageNolSatuGorontalo = np.divide(cleanNolSatuGorontalo, cleanTotalSuaraGorontalo)*100
percentageNolSatuGorontaloSeries = pd.Series(percentageNolSatuGorontalo,
                                        name = "Distribusi Persentase Suara 01 di Gorontalo")

plotDistribusiGorontalo, seabornGorontalo = plt.subplots()
sns.distplot(percentageNolSatuGorontaloSeries, kde=False, bins=100, ax = seabornGorontalo)
plotDistribusiGorontalo.savefig("Gorontalo.png")

jambiData = pd.read_csv("Jambi.csv")

nolSatuJambi = jambiData["01 KPU"]
nolDuaJambi = jambiData["02 KPU"]

cleanNolSatuJambi = []
cleanNolDuaJambi = []

for x in range(len(nolSatuJambi)):
    if nolSatuJambi[x] == 0 and nolDuaJambi[x] == 0:
        continue
    else:
        cleanNolSatuJambi.append(nolSatuJambi[x])
        cleanNolDuaJambi.append(nolDuaJambi[x])
        
cleanTotalSuaraJambi = np.add(cleanNolSatuJambi, cleanNolDuaJambi)

percentageNolSatuJambi = np.divide(cleanNolSatuJambi, cleanTotalSuaraJambi)*100
percentageNolSatuJambiSeries = pd.Series(percentageNolSatuJambi,
                                        name = "Distribusi Persentase Suara 01 di Jambi")

plotDistribusiJambi, seabornJambi = plt.subplots()
sns.distplot(percentageNolSatuJambiSeries, kde=False, bins=100, ax = seabornJambi)
plotDistribusiJambi.savefig("Jambi.png")

jawaBaratData = pd.read_csv("JawaBarat.csv")

nolSatuJawaBarat = jawaBaratData["01 KPU"]
nolDuaJawaBarat = jawaBaratData["02 KPU"]

cleanNolSatuJawaBarat = []
cleanNolDuaJawaBarat = []

for x in range(len(nolSatuJawaBarat)):
    if nolSatuJawaBarat[x] == 0 and nolDuaJawaBarat[x] == 0:
        continue
    else:
        cleanNolSatuJawaBarat.append(nolSatuJawaBarat[x])
        cleanNolDuaJawaBarat.append(nolDuaJawaBarat[x])
        
cleanTotalSuaraJawaBarat = np.add(cleanNolSatuJawaBarat, cleanNolDuaJawaBarat)

percentageNolSatuJawaBarat = np.divide(cleanNolSatuJawaBarat, cleanTotalSuaraJawaBarat)*100
percentageNolSatuJawaBaratSeries = pd.Series(percentageNolSatuJawaBarat,
                                        name = "Distribusi Persentase Suara 01 di JawaBarat")

plotDistribusiJawaBarat, seabornJawaBarat = plt.subplots()
sns.distplot(percentageNolSatuJawaBaratSeries, kde=False, bins=100, ax = seabornJawaBarat)
plotDistribusiJawaBarat.savefig("JawaBarat.png")

jawaTengahData = pd.read_csv("JawaTengah.csv")

nolSatuJawaTengah = jawaTengahData["01 KPU"]
nolDuaJawaTengah = jawaTengahData["02 KPU"]

cleanNolSatuJawaTengah = []
cleanNolDuaJawaTengah = []

for x in range(len(nolSatuJawaTengah)):
    if nolSatuJawaTengah[x] == 0 and nolDuaJawaTengah[x] == 0:
        continue
    else:
        cleanNolSatuJawaTengah.append(nolSatuJawaTengah[x])
        cleanNolDuaJawaTengah.append(nolDuaJawaTengah[x])
        
cleanTotalSuaraJawaTengah = np.add(cleanNolSatuJawaTengah, cleanNolDuaJawaTengah)

percentageNolSatuJawaTengah = np.divide(cleanNolSatuJawaTengah, cleanTotalSuaraJawaTengah)*100
percentageNolSatuJawaTengahSeries = pd.Series(percentageNolSatuJawaTengah,
                                        name = "Distribusi Persentase Suara 01 di JawaTengah")

plotDistribusiJawaTengah, seabornJawaTengah = plt.subplots()
sns.distplot(percentageNolSatuJawaTengahSeries, kde=False, bins=100, ax = seabornJawaTengah)
plotDistribusiJawaTengah.savefig("JawaTengah.png")

jawaTimurData = pd.read_csv("JawaTimur.csv")

nolSatuJawaTimur = jawaTimurData["01 KPU"]
nolDuaJawaTimur = jawaTimurData["02 KPU"]

cleanNolSatuJawaTimur = []
cleanNolDuaJawaTimur = []

for x in range(len(nolSatuJawaTimur)):
    if nolSatuJawaTimur[x] == 0 and nolDuaJawaTimur[x] == 0:
        continue
    else:
        cleanNolSatuJawaTimur.append(nolSatuJawaTimur[x])
        cleanNolDuaJawaTimur.append(nolDuaJawaTimur[x])
        
cleanTotalSuaraJawaTimur = np.add(cleanNolSatuJawaTimur, cleanNolDuaJawaTimur)

percentageNolSatuJawaTimur = np.divide(cleanNolSatuJawaTimur, cleanTotalSuaraJawaTimur)*100
percentageNolSatuJawaTimurSeries = pd.Series(percentageNolSatuJawaTimur,
                                        name = "Distribusi Persentase Suara 01 di JawaTimur")

plotDistribusiJawaTimur, seabornJawaTimur = plt.subplots()
sns.distplot(percentageNolSatuJawaTimurSeries, kde=False, bins=100, ax = seabornJawaTimur)
plotDistribusiJawaTimur.savefig("JawaTimur.png")

kalimantanBaratData = pd.read_csv("KalimantanBarat.csv")

nolSatuKalimantanBarat = kalimantanBaratData["01 KPU"]
nolDuaKalimantanBarat = kalimantanBaratData["02 KPU"]

cleanNolSatuKalimantanBarat = []
cleanNolDuaKalimantanBarat = []

for x in range(len(nolSatuKalimantanBarat)):
    if nolSatuKalimantanBarat[x] == 0 and nolDuaKalimantanBarat[x] == 0:
        continue
    else:
        cleanNolSatuKalimantanBarat.append(nolSatuKalimantanBarat[x])
        cleanNolDuaKalimantanBarat.append(nolDuaKalimantanBarat[x])
        
cleanTotalSuaraKalimantanBarat = np.add(cleanNolSatuKalimantanBarat, cleanNolDuaKalimantanBarat)

percentageNolSatuKalimantanBarat = np.divide(cleanNolSatuKalimantanBarat, cleanTotalSuaraKalimantanBarat)*100
percentageNolSatuKalimantanBaratSeries = pd.Series(percentageNolSatuKalimantanBarat,
                                        name = "Distribusi Persentase Suara 01 di KalimantanBarat")

plotDistribusiKalimantanBarat, seabornKalimantanBarat = plt.subplots()
sns.distplot(percentageNolSatuKalimantanBaratSeries, kde=False, bins=100, ax = seabornKalimantanBarat)
plotDistribusiKalimantanBarat.savefig("KalimantanBarat.png")

kalimantanSelatanData = pd.read_csv("KalimantanSelatan.csv")

nolSatuKalimantanSelatan = kalimantanSelatanData["01 KPU"]
nolDuaKalimantanSelatan = kalimantanSelatanData["02 KPU"]

cleanNolSatuKalimantanSelatan = []
cleanNolDuaKalimantanSelatan = []

for x in range(len(nolSatuKalimantanSelatan)):
    if nolSatuKalimantanSelatan[x] == 0 and nolDuaKalimantanSelatan[x] == 0:
        continue
    else:
        cleanNolSatuKalimantanSelatan.append(nolSatuKalimantanSelatan[x])
        cleanNolDuaKalimantanSelatan.append(nolDuaKalimantanSelatan[x])
        
cleanTotalSuaraKalimantanSelatan = np.add(cleanNolSatuKalimantanSelatan, cleanNolDuaKalimantanSelatan)

percentageNolSatuKalimantanSelatan = np.divide(cleanNolSatuKalimantanSelatan, cleanTotalSuaraKalimantanSelatan)*100
percentageNolSatuKalimantanSelatanSeries = pd.Series(percentageNolSatuKalimantanSelatan,
                                        name = "Distribusi Persentase Suara 01 di KalimantanSelatan")

plotDistribusiKalimantanSelatan, seabornKalimantanSelatan = plt.subplots()
sns.distplot(percentageNolSatuKalimantanSelatanSeries, kde=False, bins=100, ax = seabornKalimantanSelatan)
plotDistribusiKalimantanSelatan.savefig("KalimantanSelatan.png")

kalimantanTengahData = pd.read_csv("KalimantanTengah.csv")

nolSatuKalimantanTengah = kalimantanTengahData["01 KPU"]
nolDuaKalimantanTengah = kalimantanTengahData["02 KPU"]

cleanNolSatuKalimantanTengah = []
cleanNolDuaKalimantanTengah = []

for x in range(len(nolSatuKalimantanTengah)):
    if nolSatuKalimantanTengah[x] == 0 and nolDuaKalimantanTengah[x] == 0:
        continue
    else:
        cleanNolSatuKalimantanTengah.append(nolSatuKalimantanTengah[x])
        cleanNolDuaKalimantanTengah.append(nolDuaKalimantanTengah[x])
        
cleanTotalSuaraKalimantanTengah = np.add(cleanNolSatuKalimantanTengah, cleanNolDuaKalimantanTengah)

percentageNolSatuKalimantanTengah = np.divide(cleanNolSatuKalimantanTengah, cleanTotalSuaraKalimantanTengah)*100
percentageNolSatuKalimantanTengahSeries = pd.Series(percentageNolSatuKalimantanTengah,
                                        name = "Distribusi Persentase Suara 01 di KalimantanTengah")

plotDistribusiKalimantanTengah, seabornKalimantanTengah = plt.subplots()
sns.distplot(percentageNolSatuKalimantanTengahSeries, kde=False, bins=100, ax = seabornKalimantanTengah)
plotDistribusiKalimantanTengah.savefig("KalimantanTengah.png")

kalimantanTimurData = pd.read_csv("KalimantanTimur.csv")

nolSatuKalimantanTimur = kalimantanTimurData["01 KPU"]
nolDuaKalimantanTimur = kalimantanTimurData["02 KPU"]

cleanNolSatuKalimantanTimur = []
cleanNolDuaKalimantanTimur = []

for x in range(len(nolSatuKalimantanTimur)):
    if nolSatuKalimantanTimur[x] == 0 and nolDuaKalimantanTimur[x] == 0:
        continue
    else:
        cleanNolSatuKalimantanTimur.append(nolSatuKalimantanTimur[x])
        cleanNolDuaKalimantanTimur.append(nolDuaKalimantanTimur[x])
        
cleanTotalSuaraKalimantanTimur = np.add(cleanNolSatuKalimantanTimur, cleanNolDuaKalimantanTimur)

percentageNolSatuKalimantanTimur = np.divide(cleanNolSatuKalimantanTimur, cleanTotalSuaraKalimantanTimur)*100
percentageNolSatuKalimantanTimurSeries = pd.Series(percentageNolSatuKalimantanTimur,
                                        name = "Distribusi Persentase Suara 01 di KalimantanTimur")

plotDistribusiKalimantanTimur, seabornKalimantanTimur = plt.subplots()
sns.distplot(percentageNolSatuKalimantanTimurSeries, kde=False, bins=100, ax = seabornKalimantanTimur)
plotDistribusiKalimantanTimur.savefig("KalimantanTimur.png")

kalimantanUtaraData = pd.read_csv("KalimantanUtara.csv")

nolSatuKalimantanUtara = kalimantanUtaraData["01 KPU"]
nolDuaKalimantanUtara = kalimantanUtaraData["02 KPU"]

cleanNolSatuKalimantanUtara = []
cleanNolDuaKalimantanUtara = []

for x in range(len(nolSatuKalimantanUtara)):
    if nolSatuKalimantanUtara[x] == 0 and nolDuaKalimantanUtara[x] == 0:
        continue
    else:
        cleanNolSatuKalimantanUtara.append(nolSatuKalimantanUtara[x])
        cleanNolDuaKalimantanUtara.append(nolDuaKalimantanUtara[x])
        
cleanTotalSuaraKalimantanUtara = np.add(cleanNolSatuKalimantanUtara, cleanNolDuaKalimantanUtara)

percentageNolSatuKalimantanUtara = np.divide(cleanNolSatuKalimantanUtara, cleanTotalSuaraKalimantanUtara)*100
percentageNolSatuKalimantanUtaraSeries = pd.Series(percentageNolSatuKalimantanUtara,
                                        name = "Distribusi Persentase Suara 01 di KalimantanUtara")

plotDistribusiKalimantanUtara, seabornKalimantanUtara = plt.subplots()
sns.distplot(percentageNolSatuKalimantanUtaraSeries, kde=False, bins=100, ax = seabornKalimantanUtara)
plotDistribusiKalimantanUtara.savefig("KalimantanUtara.png")

kepulauanBangkaData = pd.read_csv("KepulauanBangka.csv")

nolSatuKepulauanBangka = kepulauanBangkaData["01 KPU"]
nolDuaKepulauanBangka = kepulauanBangkaData["02 KPU"]

cleanNolSatuKepulauanBangka = []
cleanNolDuaKepulauanBangka = []

for x in range(len(nolSatuKepulauanBangka)):
    if nolSatuKepulauanBangka[x] == 0 and nolDuaKepulauanBangka[x] == 0:
        continue
    else:
        cleanNolSatuKepulauanBangka.append(nolSatuKepulauanBangka[x])
        cleanNolDuaKepulauanBangka.append(nolDuaKepulauanBangka[x])
        
cleanTotalSuaraKepulauanBangka = np.add(cleanNolSatuKepulauanBangka, cleanNolDuaKepulauanBangka)

percentageNolSatuKepulauanBangka = np.divide(cleanNolSatuKepulauanBangka, cleanTotalSuaraKepulauanBangka)*100
percentageNolSatuKepulauanBangkaSeries = pd.Series(percentageNolSatuKepulauanBangka,
                                        name = "Distribusi Persentase Suara 01 di KepulauanBangka")

plotDistribusiKepulauanBangka, seabornKepulauanBangka = plt.subplots()
sns.distplot(percentageNolSatuKepulauanBangkaSeries, kde=False, bins=100, ax = seabornKepulauanBangka)
plotDistribusiKepulauanBangka.savefig("KepulauanBangka.png")

kepulauanRiauData = pd.read_csv("KepulauanRiau.csv")

nolSatuKepulauanRiau = kepulauanRiauData["01 KPU"]
nolDuaKepulauanRiau = kepulauanRiauData["02 KPU"]

cleanNolSatuKepulauanRiau = []
cleanNolDuaKepulauanRiau = []

for x in range(len(nolSatuKepulauanRiau)):
    if nolSatuKepulauanRiau[x] == 0 and nolDuaKepulauanRiau[x] == 0:
        continue
    else:
        cleanNolSatuKepulauanRiau.append(nolSatuKepulauanRiau[x])
        cleanNolDuaKepulauanRiau.append(nolDuaKepulauanRiau[x])
        
cleanTotalSuaraKepulauanRiau = np.add(cleanNolSatuKepulauanRiau, cleanNolDuaKepulauanRiau)

percentageNolSatuKepulauanRiau = np.divide(cleanNolSatuKepulauanRiau, cleanTotalSuaraKepulauanRiau)*100
percentageNolSatuKepulauanRiauSeries = pd.Series(percentageNolSatuKepulauanRiau,
                                        name = "Distribusi Persentase Suara 01 di KepulauanRiau")

plotDistribusiKepulauanRiau, seabornKepulauanRiau = plt.subplots()
sns.distplot(percentageNolSatuKepulauanRiauSeries, kde=False, bins=100, ax = seabornKepulauanRiau)
plotDistribusiKepulauanRiau.savefig("KepulauanRiau.png")

lampungData = pd.read_csv("Lampung.csv")

nolSatuLampung = lampungData["01 KPU"]
nolDuaLampung = lampungData["02 KPU"]

cleanNolSatuLampung = []
cleanNolDuaLampung = []

for x in range(len(nolSatuLampung)):
    if nolSatuLampung[x] == 0 and nolDuaLampung[x] == 0:
        continue
    else:
        cleanNolSatuLampung.append(nolSatuLampung[x])
        cleanNolDuaLampung.append(nolDuaLampung[x])
        
cleanTotalSuaraLampung = np.add(cleanNolSatuLampung, cleanNolDuaLampung)

percentageNolSatuLampung = np.divide(cleanNolSatuLampung, cleanTotalSuaraLampung)*100
percentageNolSatuLampungSeries = pd.Series(percentageNolSatuLampung,
                                        name = "Distribusi Persentase Suara 01 di Lampung")

plotDistribusiLampung, seabornLampung = plt.subplots()
sns.distplot(percentageNolSatuLampungSeries, kde=False, bins=100, ax = seabornLampung)
plotDistribusiLampung.savefig("Lampung.png")

malukuData = pd.read_csv("Maluku.csv")

nolSatuMaluku = malukuData["01 KPU"]
nolDuaMaluku = malukuData["02 KPU"]

cleanNolSatuMaluku = []
cleanNolDuaMaluku = []

for x in range(len(nolSatuMaluku)):
    if nolSatuMaluku[x] == 0 and nolDuaMaluku[x] == 0:
        continue
    else:
        cleanNolSatuMaluku.append(nolSatuMaluku[x])
        cleanNolDuaMaluku.append(nolDuaMaluku[x])
        
cleanTotalSuaraMaluku = np.add(cleanNolSatuMaluku, cleanNolDuaMaluku)

percentageNolSatuMaluku = np.divide(cleanNolSatuMaluku, cleanTotalSuaraMaluku)*100
percentageNolSatuMalukuSeries = pd.Series(percentageNolSatuMaluku,
                                        name = "Distribusi Persentase Suara 01 di Maluku")

plotDistribusiMaluku, seabornMaluku = plt.subplots()
sns.distplot(percentageNolSatuMalukuSeries, kde=False, bins=100, ax = seabornMaluku)
plotDistribusiMaluku.savefig("Maluku.png")

malukuUtaraData = pd.read_csv("MalukuUtara.csv")

nolSatuMalukuUtara = malukuUtaraData["01 KPU"]
nolDuaMalukuUtara = malukuUtaraData["02 KPU"]

cleanNolSatuMalukuUtara = []
cleanNolDuaMalukuUtara = []

for x in range(len(nolSatuMalukuUtara)):
    if nolSatuMalukuUtara[x] == 0 and nolDuaMalukuUtara[x] == 0:
        continue
    else:
        cleanNolSatuMalukuUtara.append(nolSatuMalukuUtara[x])
        cleanNolDuaMalukuUtara.append(nolDuaMalukuUtara[x])
        
cleanTotalSuaraMalukuUtara = np.add(cleanNolSatuMalukuUtara, cleanNolDuaMalukuUtara)

percentageNolSatuMalukuUtara = np.divide(cleanNolSatuMalukuUtara, cleanTotalSuaraMalukuUtara)*100
percentageNolSatuMalukuUtaraSeries = pd.Series(percentageNolSatuMalukuUtara,
                                        name = "Distribusi Persentase Suara 01 di MalukuUtara")

plotDistribusiMalukuUtara, seabornMalukuUtara = plt.subplots()
sns.distplot(percentageNolSatuMalukuUtaraSeries, kde=False, bins=100, ax = seabornMalukuUtara)
plotDistribusiMalukuUtara.savefig("MalukuUtara.png")

nusaTenggaraBaratData = pd.read_csv("NusaTenggaraBarat.csv")

nolSatuNusaTenggaraBarat = nusaTenggaraBaratData["01 KPU"]
nolDuaNusaTenggaraBarat = nusaTenggaraBaratData["02 KPU"]

cleanNolSatuNusaTenggaraBarat = []
cleanNolDuaNusaTenggaraBarat = []

for x in range(len(nolSatuNusaTenggaraBarat)):
    if nolSatuNusaTenggaraBarat[x] == 0 and nolDuaNusaTenggaraBarat[x] == 0:
        continue
    else:
        cleanNolSatuNusaTenggaraBarat.append(nolSatuNusaTenggaraBarat[x])
        cleanNolDuaNusaTenggaraBarat.append(nolDuaNusaTenggaraBarat[x])
        
cleanTotalSuaraNusaTenggaraBarat = np.add(cleanNolSatuNusaTenggaraBarat, cleanNolDuaNusaTenggaraBarat)

percentageNolSatuNusaTenggaraBarat = np.divide(cleanNolSatuNusaTenggaraBarat, cleanTotalSuaraNusaTenggaraBarat)*100
percentageNolSatuNusaTenggaraBaratSeries = pd.Series(percentageNolSatuNusaTenggaraBarat,
                                        name = "Distribusi Persentase Suara 01 di NusaTenggaraBarat")

plotDistribusiNusaTenggaraBarat, seabornNusaTenggaraBarat = plt.subplots()
sns.distplot(percentageNolSatuNusaTenggaraBaratSeries, kde=False, bins=100, ax = seabornNusaTenggaraBarat)
plotDistribusiNusaTenggaraBarat.savefig("NusaTenggaraBarat.png")

nusaTenggaraTimurData = pd.read_csv("NusaTenggaraTimur.csv")

nolSatuNusaTenggaraTimur = nusaTenggaraTimurData["01 KPU"]
nolDuaNusaTenggaraTimur = nusaTenggaraTimurData["02 KPU"]

cleanNolSatuNusaTenggaraTimur = []
cleanNolDuaNusaTenggaraTimur = []

for x in range(len(nolSatuNusaTenggaraTimur)):
    if nolSatuNusaTenggaraTimur[x] == 0 and nolDuaNusaTenggaraTimur[x] == 0:
        continue
    else:
        cleanNolSatuNusaTenggaraTimur.append(nolSatuNusaTenggaraTimur[x])
        cleanNolDuaNusaTenggaraTimur.append(nolDuaNusaTenggaraTimur[x])
        
cleanTotalSuaraNusaTenggaraTimur = np.add(cleanNolSatuNusaTenggaraTimur, cleanNolDuaNusaTenggaraTimur)

percentageNolSatuNusaTenggaraTimur = np.divide(cleanNolSatuNusaTenggaraTimur, cleanTotalSuaraNusaTenggaraTimur)*100
percentageNolSatuNusaTenggaraTimurSeries = pd.Series(percentageNolSatuNusaTenggaraTimur,
                                        name = "Distribusi Persentase Suara 01 di NusaTenggaraTimur")

plotDistribusiNusaTenggaraTimur, seabornNusaTenggaraTimur = plt.subplots()
sns.distplot(percentageNolSatuNusaTenggaraTimurSeries, kde=False, bins=100, ax = seabornNusaTenggaraTimur)
plotDistribusiNusaTenggaraTimur.savefig("NusaTenggaraTimur.png")

papuaData = pd.read_csv("Papua.csv")

nolSatuPapua = papuaData["01 KPU"]
nolDuaPapua = papuaData["02 KPU"]

cleanNolSatuPapua = []
cleanNolDuaPapua = []

for x in range(len(nolSatuPapua)):
    if nolSatuPapua[x] == 0 and nolDuaPapua[x] == 0:
        continue
    else:
        cleanNolSatuPapua.append(nolSatuPapua[x])
        cleanNolDuaPapua.append(nolDuaPapua[x])
        
cleanTotalSuaraPapua = np.add(cleanNolSatuPapua, cleanNolDuaPapua)

percentageNolSatuPapua = np.divide(cleanNolSatuPapua, cleanTotalSuaraPapua)*100
percentageNolSatuPapuaSeries = pd.Series(percentageNolSatuPapua,
                                        name = "Distribusi Persentase Suara 01 di Papua")

plotDistribusiPapua, seabornPapua = plt.subplots()
sns.distplot(percentageNolSatuPapuaSeries, kde=False, bins=100, ax = seabornPapua)
plotDistribusiPapua.savefig("Papua.png")

papuaBaratData = pd.read_csv("PapuaBarat.csv")

nolSatuPapuaBarat = papuaBaratData["01 KPU"]
nolDuaPapuaBarat = papuaBaratData["02 KPU"]

cleanNolSatuPapuaBarat = []
cleanNolDuaPapuaBarat = []

for x in range(len(nolSatuPapuaBarat)):
    if nolSatuPapuaBarat[x] == 0 and nolDuaPapuaBarat[x] == 0:
        continue
    else:
        cleanNolSatuPapuaBarat.append(nolSatuPapuaBarat[x])
        cleanNolDuaPapuaBarat.append(nolDuaPapuaBarat[x])
        
cleanTotalSuaraPapuaBarat = np.add(cleanNolSatuPapuaBarat, cleanNolDuaPapuaBarat)

percentageNolSatuPapuaBarat = np.divide(cleanNolSatuPapuaBarat, cleanTotalSuaraPapuaBarat)*100
percentageNolSatuPapuaBaratSeries = pd.Series(percentageNolSatuPapuaBarat,
                                        name = "Distribusi Persentase Suara 01 di PapuaBarat")

plotDistribusiPapuaBarat, seabornPapuaBarat = plt.subplots()
sns.distplot(percentageNolSatuPapuaBaratSeries, kde=False, bins=100, ax = seabornPapuaBarat)
plotDistribusiPapuaBarat.savefig("PapuaBarat.png")

riauData = pd.read_csv("Riau.csv")

nolSatuRiau = riauData["01 KPU"]
nolDuaRiau = riauData["02 KPU"]

cleanNolSatuRiau = []
cleanNolDuaRiau = []

for x in range(len(nolSatuRiau)):
    if nolSatuRiau[x] == 0 and nolDuaRiau[x] == 0:
        continue
    else:
        cleanNolSatuRiau.append(nolSatuRiau[x])
        cleanNolDuaRiau.append(nolDuaRiau[x])
        
cleanTotalSuaraRiau = np.add(cleanNolSatuRiau, cleanNolDuaRiau)

percentageNolSatuRiau = np.divide(cleanNolSatuRiau, cleanTotalSuaraRiau)*100
percentageNolSatuRiauSeries = pd.Series(percentageNolSatuRiau,
                                        name = "Distribusi Persentase Suara 01 di Riau")

plotDistribusiRiau, seabornRiau = plt.subplots()
sns.distplot(percentageNolSatuRiauSeries, kde=False, bins=100, ax = seabornRiau)
plotDistribusiRiau.savefig("Riau.png")

sulawesiBaratData = pd.read_csv("SulawesiBarat.csv")

nolSatuSulawesiBarat = sulawesiBaratData["01 KPU"]
nolDuaSulawesiBarat = sulawesiBaratData["02 KPU"]

cleanNolSatuSulawesiBarat = []
cleanNolDuaSulawesiBarat = []

for x in range(len(nolSatuSulawesiBarat)):
    if nolSatuSulawesiBarat[x] == 0 and nolDuaSulawesiBarat[x] == 0:
        continue
    else:
        cleanNolSatuSulawesiBarat.append(nolSatuSulawesiBarat[x])
        cleanNolDuaSulawesiBarat.append(nolDuaSulawesiBarat[x])
        
cleanTotalSuaraSulawesiBarat = np.add(cleanNolSatuSulawesiBarat, cleanNolDuaSulawesiBarat)

percentageNolSatuSulawesiBarat = np.divide(cleanNolSatuSulawesiBarat, cleanTotalSuaraSulawesiBarat)*100
percentageNolSatuSulawesiBaratSeries = pd.Series(percentageNolSatuSulawesiBarat,
                                        name = "Distribusi Persentase Suara 01 di SulawesiBarat")

plotDistribusiSulawesiBarat, seabornSulawesiBarat = plt.subplots()
sns.distplot(percentageNolSatuSulawesiBaratSeries, kde=False, bins=100, ax = seabornSulawesiBarat)
plotDistribusiSulawesiBarat.savefig("SulawesiBarat.png")

sulawesiSelatanData = pd.read_csv("SulawesiSelatan.csv")

nolSatuSulawesiSelatan = sulawesiSelatanData["01 KPU"]
nolDuaSulawesiSelatan = sulawesiSelatanData["02 KPU"]

cleanNolSatuSulawesiSelatan = []
cleanNolDuaSulawesiSelatan = []

for x in range(len(nolSatuSulawesiSelatan)):
    if nolSatuSulawesiSelatan[x] == 0 and nolDuaSulawesiSelatan[x] == 0:
        continue
    else:
        cleanNolSatuSulawesiSelatan.append(nolSatuSulawesiSelatan[x])
        cleanNolDuaSulawesiSelatan.append(nolDuaSulawesiSelatan[x])
        
cleanTotalSuaraSulawesiSelatan = np.add(cleanNolSatuSulawesiSelatan, cleanNolDuaSulawesiSelatan)

percentageNolSatuSulawesiSelatan = np.divide(cleanNolSatuSulawesiSelatan, cleanTotalSuaraSulawesiSelatan)*100
percentageNolSatuSulawesiSelatanSeries = pd.Series(percentageNolSatuSulawesiSelatan,
                                        name = "Distribusi Persentase Suara 01 di SulawesiSelatan")

plotDistribusiSulawesiSelatan, seabornSulawesiSelatan = plt.subplots()
sns.distplot(percentageNolSatuSulawesiSelatanSeries, kde=False, bins=100, ax = seabornSulawesiSelatan)
plotDistribusiSulawesiSelatan.savefig("SulawesiSelatan.png")

sulawesiTengahData = pd.read_csv("SulawesiTengah.csv")

nolSatuSulawesiTengah = sulawesiTengahData["01 KPU"]
nolDuaSulawesiTengah = sulawesiTengahData["02 KPU"]

cleanNolSatuSulawesiTengah = []
cleanNolDuaSulawesiTengah = []

for x in range(len(nolSatuSulawesiTengah)):
    if nolSatuSulawesiTengah[x] == 0 and nolDuaSulawesiTengah[x] == 0:
        continue
    else:
        cleanNolSatuSulawesiTengah.append(nolSatuSulawesiTengah[x])
        cleanNolDuaSulawesiTengah.append(nolDuaSulawesiTengah[x])
        
cleanTotalSuaraSulawesiTengah = np.add(cleanNolSatuSulawesiTengah, cleanNolDuaSulawesiTengah)

percentageNolSatuSulawesiTengah = np.divide(cleanNolSatuSulawesiTengah, cleanTotalSuaraSulawesiTengah)*100
percentageNolSatuSulawesiTengahSeries = pd.Series(percentageNolSatuSulawesiTengah,
                                        name = "Distribusi Persentase Suara 01 di SulawesiTengah")

plotDistribusiSulawesiTengah, seabornSulawesiTengah = plt.subplots()
sns.distplot(percentageNolSatuSulawesiTengahSeries, kde=False, bins=100, ax = seabornSulawesiTengah)
plotDistribusiSulawesiTengah.savefig("SulawesiTengah.png")

sulawesiTenggaraData = pd.read_csv("SulawesiTenggara.csv")

nolSatuSulawesiTenggara = sulawesiTenggaraData["01 KPU"]
nolDuaSulawesiTenggara = sulawesiTenggaraData["02 KPU"]

cleanNolSatuSulawesiTenggara = []
cleanNolDuaSulawesiTenggara = []

for x in range(len(nolSatuSulawesiTenggara)):
    if nolSatuSulawesiTenggara[x] == 0 and nolDuaSulawesiTenggara[x] == 0:
        continue
    else:
        cleanNolSatuSulawesiTenggara.append(nolSatuSulawesiTenggara[x])
        cleanNolDuaSulawesiTenggara.append(nolDuaSulawesiTenggara[x])
        
cleanTotalSuaraSulawesiTenggara = np.add(cleanNolSatuSulawesiTenggara, cleanNolDuaSulawesiTenggara)

percentageNolSatuSulawesiTenggara = np.divide(cleanNolSatuSulawesiTenggara, cleanTotalSuaraSulawesiTenggara)*100
percentageNolSatuSulawesiTenggaraSeries = pd.Series(percentageNolSatuSulawesiTenggara,
                                        name = "Distribusi Persentase Suara 01 di SulawesiTenggara")

plotDistribusiSulawesiTenggara, seabornSulawesiTenggara = plt.subplots()
sns.distplot(percentageNolSatuSulawesiTenggaraSeries, kde=False, bins=100, ax = seabornSulawesiTenggara)
plotDistribusiSulawesiTenggara.savefig("SulawesiTenggara.png")

sulawesiUtaraData = pd.read_csv("SulawesiUtara.csv")

nolSatuSulawesiUtara = sulawesiUtaraData["01 KPU"]
nolDuaSulawesiUtara = sulawesiUtaraData["02 KPU"]

cleanNolSatuSulawesiUtara = []
cleanNolDuaSulawesiUtara = []

for x in range(len(nolSatuSulawesiUtara)):
    if nolSatuSulawesiUtara[x] == 0 and nolDuaSulawesiUtara[x] == 0:
        continue
    else:
        cleanNolSatuSulawesiUtara.append(nolSatuSulawesiUtara[x])
        cleanNolDuaSulawesiUtara.append(nolDuaSulawesiUtara[x])
        
cleanTotalSuaraSulawesiUtara = np.add(cleanNolSatuSulawesiUtara, cleanNolDuaSulawesiUtara)

percentageNolSatuSulawesiUtara = np.divide(cleanNolSatuSulawesiUtara, cleanTotalSuaraSulawesiUtara)*100
percentageNolSatuSulawesiUtaraSeries = pd.Series(percentageNolSatuSulawesiUtara,
                                        name = "Distribusi Persentase Suara 01 di SulawesiUtara")

plotDistribusiSulawesiUtara, seabornSulawesiUtara = plt.subplots()
sns.distplot(percentageNolSatuSulawesiUtaraSeries, kde=False, bins=100, ax = seabornSulawesiUtara)
plotDistribusiSulawesiUtara.savefig("SulawesiUtara.png")

sumateraBaratData = pd.read_csv("SumateraBarat.csv")

nolSatuSumateraBarat = sumateraBaratData["01 KPU"]
nolDuaSumateraBarat = sumateraBaratData["02 KPU"]

cleanNolSatuSumateraBarat = []
cleanNolDuaSumateraBarat = []

for x in range(len(nolSatuSumateraBarat)):
    if nolSatuSumateraBarat[x] == 0 and nolDuaSumateraBarat[x] == 0:
        continue
    else:
        cleanNolSatuSumateraBarat.append(nolSatuSumateraBarat[x])
        cleanNolDuaSumateraBarat.append(nolDuaSumateraBarat[x])
        
cleanTotalSuaraSumateraBarat = np.add(cleanNolSatuSumateraBarat, cleanNolDuaSumateraBarat)

percentageNolSatuSumateraBarat = np.divide(cleanNolSatuSumateraBarat, cleanTotalSuaraSumateraBarat)*100
percentageNolSatuSumateraBaratSeries = pd.Series(percentageNolSatuSumateraBarat,
                                        name = "Distribusi Persentase Suara 01 di SumateraBarat")

plotDistribusiSumateraBarat, seabornSumateraBarat = plt.subplots()
sns.distplot(percentageNolSatuSumateraBaratSeries, kde=False, bins=100, ax = seabornSumateraBarat)
plotDistribusiSumateraBarat.savefig("SumateraBarat.png")

sumateraSelatanData = pd.read_csv("SumateraSelatan.csv")

nolSatuSumateraSelatan = sumateraSelatanData["01 KPU"]
nolDuaSumateraSelatan = sumateraSelatanData["02 KPU"]

cleanNolSatuSumateraSelatan = []
cleanNolDuaSumateraSelatan = []

for x in range(len(nolSatuSumateraSelatan)):
    if nolSatuSumateraSelatan[x] == 0 and nolDuaSumateraSelatan[x] == 0:
        continue
    else:
        cleanNolSatuSumateraSelatan.append(nolSatuSumateraSelatan[x])
        cleanNolDuaSumateraSelatan.append(nolDuaSumateraSelatan[x])
        
cleanTotalSuaraSumateraSelatan = np.add(cleanNolSatuSumateraSelatan, cleanNolDuaSumateraSelatan)

percentageNolSatuSumateraSelatan = np.divide(cleanNolSatuSumateraSelatan, cleanTotalSuaraSumateraSelatan)*100
percentageNolSatuSumateraSelatanSeries = pd.Series(percentageNolSatuSumateraSelatan,
                                        name = "Distribusi Persentase Suara 01 di SumateraSelatan")

plotDistribusiSumateraSelatan, seabornSumateraSelatan = plt.subplots()
sns.distplot(percentageNolSatuSumateraSelatanSeries, kde=False, bins=100, ax = seabornSumateraSelatan)
plotDistribusiSumateraSelatan.savefig("SumateraSelatan.png")

sumateraUtaraData = pd.read_csv("SumateraUtara.csv")

nolSatuSumateraUtara = sumateraUtaraData["01 KPU"]
nolDuaSumateraUtara = sumateraUtaraData["02 KPU"]

cleanNolSatuSumateraUtara = []
cleanNolDuaSumateraUtara = []

for x in range(len(nolSatuSumateraUtara)):
    if nolSatuSumateraUtara[x] == 0 and nolDuaSumateraUtara[x] == 0:
        continue
    else:
        cleanNolSatuSumateraUtara.append(nolSatuSumateraUtara[x])
        cleanNolDuaSumateraUtara.append(nolDuaSumateraUtara[x])
        
cleanTotalSuaraSumateraUtara = np.add(cleanNolSatuSumateraUtara, cleanNolDuaSumateraUtara)

percentageNolSatuSumateraUtara = np.divide(cleanNolSatuSumateraUtara, cleanTotalSuaraSumateraUtara)*100
percentageNolSatuSumateraUtaraSeries = pd.Series(percentageNolSatuSumateraUtara,
                                        name = "Distribusi Persentase Suara 01 di SumateraUtara")

plotDistribusiSumateraUtara, seabornSumateraUtara = plt.subplots()
sns.distplot(percentageNolSatuSumateraUtaraSeries, kde=False, bins=100, ax = seabornSumateraUtara)
plotDistribusiSumateraUtara.savefig("SumateraUtara.png")