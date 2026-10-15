import pandas as pd 
# datayı ele almayı saglayan kutuphane

grades = {"Batu": 50, "James": 60, "Lars": 30}

print(pd.Series(grades)) # tek boyutlu array gibi davranır 

print("**************************")

# arithmetic 
contestResult = pd.Series(data = [10, 5, 100], index = ["Batu", "James", "Lars"])
print(contestResult)
print("**************************")
print(contestResult["Batu"])
print("**************************")

contestResult2 = pd.Series(data = [15, 10, 150], index = ["Batu", "James", "Lars"])
print(contestResult + contestResult2) # indexlere gore toplar

# peki indexlere denk gelenler ayni olmazsa? 
print("**************************")

differentSeries = pd.Series([20,30,40,50], ["a", "b", "c", "d"])
differentSeries2 = pd.Series([10, 5, 3, 1], ["a", "c", "f", "g"])

print(differentSeries + differentSeries2) # denk gelmeyenler için NaN yani bulamadı diye bastırır
