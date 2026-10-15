import numpy as np 
import pandas as pd 

# data olusturalım yapay
data = np.random.randn(4,3) # 4'e 3'lük bir matris olustururuz
print(data)
print("*****************")

dataFrame = pd.DataFrame(data)
print(dataFrame) # data çerçevesi olusturuyor 
print("**************************")

# rowlara ve columnlara isim verelim 
newDataFrame = pd.DataFrame(data, index = ["Batu", "James", "Lars", "Tom"], columns = ["Quiz 1", "Quiz 2", "Quiz 3"])
print(newDataFrame)
print("**************************")

# bir kolonu alma 
print(newDataFrame["Quiz 2"])
print("**************************")

# birden cok kolonu alma 
print(newDataFrame[["Quiz 1", "Quiz 3"]])
print("**************************")

# sadece 1 satir alma row location'ına gore
print(newDataFrame.loc["Batu"])
print("**************************")

# sadece 1 satir alma ama row index location'ına gore
print(newDataFrame.iloc[0])
print("**************************")

#iloc ile column getirme 
print(newDataFrame.iloc[:, 0]) # : demek tum rowlari al demek ardindan , ve alinacak kolonu soyluyoruz
print("**************************")

# Data Manipulasyonu 

# kolon ekleme 
newDataFrame["Quiz 4"] = np.random.randn(4) # random degilde direkt ["Quiz 4"] = 10 yapsaydik hepsine 10 atayacakti
print(newDataFrame)
print("**************************")

# kolon silme
print(newDataFrame.drop("Quiz 4", axis = 1)) #, inplace = True) # axis = 1 kolonlar = 0 satirlar, inplace true yaparsak da kalici siler
# axis'in default degeri 0, eger degeri vermezsek satiri siler
print("**************************")

print(newDataFrame.loc["Batu"]["Quiz 1"])
print("**************************")
print(newDataFrame.loc["Batu","Quiz 1"]) # ikisi de ayni sey 
print("**************************")

newDataFrame.loc["Batu", "Quiz 1"] = 100 # deger degistirme
print(newDataFrame.loc["Batu", "Quiz 1"])
print("**************************")

# kosula gore filtreleme 
print(newDataFrame > 0)
print("**************************")



# DataFrame Index Mantigi
newIndices = ["Bat", "Jms", "Lrs", "Tm"]
newDataFrame["NewIndex"] = newIndices
print(newDataFrame)
print("**************************")

# simdi bu kolonu index yapalim 
newDataFrame.set_index("NewIndex") # inplace = True) # axis = 1 kolonlar = 0 satirlar, inplace true yaparsak da kalici siler
print(newDataFrame)
print("**************************")