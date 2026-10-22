from scipy.stats import fisher_exact
from narwhals import read_csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

import seaborn as sns 

df = pd.read_csv("17-googleplaystore.csv")
print(df.head())
print("***********************")

print(df.shape)
print("***********************")

print(df.columns)
print("***********************")

print(df.info())
print("***********************")

# missing data 
print(df.isnull().sum())
print("***********************")

# reviews aslında integer'a uygun fakat string olarak kaydedilmis 
print(f"Toplam reviews verisi sayisi : {df['Reviews'].value_counts().sum()}")
print("***********************")

print(f"integer'a uygun olanlarin sayisi: {df["Reviews"].str.isnumeric().sum()}")
print("***********************")

# 1 tane bile cevirilemeyecek olan olunca int'e cevirilemiyor
# numeric olmayani tilda (~) ile gorebiliriz
print(df[~df["Reviews"].str.isnumeric()]) # review 3.0M olarak gozukuyor 



# kopya bi df olusturalim 
dfClean = df.copy()
dfClean = dfClean.drop(dfClean.index[10472]) # 10472. satirdaki veriyi sil

# simdi int'e cevirelim 
dfClean["Reviews"] = dfClean["Reviews"].astype(int) # artik int oldu ve describe'da cikmaya basladi numericler describe'da gozukure
dfClean.info()

# simdi size kolonuna bakalim
print(dfClean["Size"].unique())
print("***********************")

# burada da 'M','k' gibi charaketer'ler var hepsini k'ye cevirelim ve m yerine 000 yazalim
dfClean["Size"] = dfClean["Size"].str.replace("M", "000")
dfClean["Size"] = dfClean["Size"].str.replace("k", "") # k'yi de kaldir
dfClean["Size"] = dfClean["Size"].replace("Varies with device", np.nan)
# Varies with device olanlari np.nan ile degistir
print(dfClean["Size"].unique())
print("***********************")

# simdi float'a cevirelim 
dfClean["Size"] = dfClean["Size"].astype(float)
print(dfClean.info())
print("***********************")

print(dfClean.isnull().sum())
print("***********************")

print(dfClean["Installs"].value_counts())
print("***********************")

print(dfClean["Installs"].unique())
print("***********************")

print(dfClean["Price"].value_counts())
print("***********************")

print(dfClean["Price"].unique())
print("***********************")

charsToRemove = ["+", ",", "$"]
colsToClean = ["Installs", "Price"]

for item in charsToRemove:
    for cols in colsToClean:
        dfClean[cols] = dfClean[cols].str.replace(item,"")

print(dfClean["Installs"].unique())
print("***********************")

print(dfClean["Price"].unique())
print("***********************")

dfClean["Price"] = dfClean["Price"].astype(float)
dfClean["Installs"] = dfClean["Installs"].astype(int)

print(dfClean.info())
print("***********************")

print(dfClean.describe()) # onceden sadece rating vardi simdi reviews size ınstalls price hepsi geldi numeric oldu
print("***********************")


# tarihle calisalim 
print(dfClean["Last Updated"])
print("***********************")

# simdi bunu datetime'a cevirelim 
dfClean["Last Updated"] = pd.to_datetime(dfClean["Last Updated"])
print(dfClean["Last Updated"])  # 2017-02-2 formatina cevirir
print("***********************")

# datayi temizledik eda'ya hazir hale getirdik, numeric ve kategorik olarak hallettik sıra EDA'delattr
# EDA 

print(dfClean.head())
print("***********************")

# duplicate var mi? 
print(dfClean.shape)
print("***********************")

print(dfClean[dfClean.duplicated("App")].shape)
print("***********************")

# 1181 satir duplicate varmis onlari silelim
dfClean.drop_duplicates(subset=["App"], keep="first", inplace=True)

print(dfClean.shape) # 10840'tan 9659'a düstü 
print("***********************")


# Sayısal olmayan her şeyi (kategorik, string, datetime) alır:
categoricalFeatures = dfClean.select_dtypes(exclude=[np.number]).columns.tolist()

# Sadece sayısal verileri alır:
numericFeatures = dfClean.select_dtypes(include=[np.number]).columns.tolist()

print(numericFeatures)
print("***********************")
print(categoricalFeatures)

plt.figure(figsize=(15,10))

for i in range(0, len(numericFeatures)):
    plt.subplot(5,3,i+1)
    sns.kdeplot(x=dfClean[numericFeatures[i]], color = "b", fill = True)
    plt.xlabel(numericFeatures[i])
    plt.tight_layout()

plt.show()
    
plt.figure(figsize=(15,5))

category = ["Type", "Content Rating"]

for i in range(0, len(category)):
    plt.subplot(1,2,i+1)
    sns.countplot(x=dfClean[category[i]], color = "b", fill=True)
    plt.xlabel(category[i])
    plt.tight_layout()
plt.show()

print(dfClean["Category"].value_counts())
print("***********************")

dfCatInstalls = dfClean.groupby(["Category"])["Installs"].sum().sort_values(ascending = False).reset_index()
dfCatInstalls["Installs"] = dfCatInstalls["Installs"] / 1000000000

# top 10 categories by install 
df2 = dfCatInstalls.head(10)
print(df2)
print("***********************")

plt.figure(figsize=(10,5))
sns.barplot(x = "Installs", y = "Category", data = df2)
plt.show()

# top 5 app in categories 
dfAppCategory = dfClean.groupby(["Category" ,"App"])["Installs"].sum().reset_index()
print(dfAppCategory)
print("***********************")

dfAppCategory = dfAppCategory.sort_values("Installs", ascending = False)

apps = ["GAME", "COMMUNICATION",  "TOOLS", "PRODUCTIVITY", "SOCIAL"]
for i , app in enumerate(apps):
    df2 = dfAppCategory[dfAppCategory.Category == app]
    df2 = df2.head(5)
    #print(df2)
    plt.figure(figsize=(40,30))
    plt.subplot(3,2,i+1)
    sns.barplot(data = df2, x = "Installs", y = "App")
    plt.title(app, size = 20)
plt.tight_layout()
plt.show()

print("***********************")

# 5 rating apps 
ratingDf = dfClean.groupby( ["Category", "Installs", "App"])["Rating"].sum().sort_values(ascending = False).reset_index()
print(ratingDf)
print("***********************")

topRatedApps = ratingDf[ratingDf["Rating"] == 5.0]
print(topRatedApps)
print("***********************")

# Android version cleaning 
dfClean["Android Ver"] = dfClean["Android Ver"].replace("and up", "", regex=True)
dfClean["Android Ver"] = dfClean["Android Ver"].replace("Varies with device", "", regex = True).replace("W", "", regex=True).replace("", np.nan)
# cizgili olanlari da yok edelim 4.1 - 7.0 gibi olanlari, zaten 10 tane app mi ne var bu formatta
dfClean = dfClean = dfClean[dfClean["Android Ver"].str.contains("-") == False] 
print(dfClean["Android Ver"].unique())
print("***********************")

# Target Encoding 
# genreslerde indirilmeye gore mean alma 
meanGenresInstalls = dfClean.groupby(["Genres"])["Installs"].mean() / 1000000 
print(meanGenresInstalls)
print("***********************")
meanGenresInstalls = meanGenresInstalls.to_dict()
dfClean["Genres Encoded"] = dfClean["Genres"].map(meanGenresInstalls)
print(dfClean.head())
print("***********************")


