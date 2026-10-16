import numpy as np
import pandas as pd 

weatherDataFrame = pd.read_excel('6-weather.xlsx')
print(weatherDataFrame)
print("******************************************************")

# bastaki ilk 5 datayi gormek 
print(weatherDataFrame.head())
print("******************************************************")

# sondaki 5 datayi gormek
print(weatherDataFrame.tail())
print("******************************************************")

# dataframe hakkinda bilgi
print(weatherDataFrame.info())
print("******************************************************")

# dataframe hakkinda istatistiksel bilgi
print(weatherDataFrame.describe())
print("******************************************************")

# bos deger var mi 
print(weatherDataFrame.isna())
print("******************************************************")

# working with missing data 
weatherNaDataFrame = pd.read_excel('6-weatherna.xlsx')
print(weatherNaDataFrame.isna()) # bazı bos degerleri gorebiliriz
print("******************************************************")

# 1 rowda bos en az 1 deger varsa o row'u silme
print(weatherNaDataFrame.dropna())
print("******************************************************")

# bos degerleri belli bir degerle doldurma
print(weatherNaDataFrame.fillna(20))
print("******************************************************")

# ya da o kolonun ortalamasıyla doldurma
print(weatherNaDataFrame.fillna(weatherNaDataFrame.mean()))
print("******************************************************")

# group by
df = pd.read_csv('6-employee.csv')
print(df)
print("******************************************************")

print(df["Salary"].mean())
print("******************************************************")

print(df[["Salary", "Experience"]].mean())
print("******************************************************")

# departmanlar hakkında detaylı bilgi verir
print(df.groupby("Department").describe())
print("******************************************************")

# departmanların maas ortalamalari
print(df.groupby("Department")["Salary"].mean())
print("******************************************************")

# Sehirlere gore maaslar
print(df.groupby("City")["Salary"].mean())