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