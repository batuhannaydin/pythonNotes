import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('TkAgg') 

df = pd.read_csv("13-WineQT.csv")

# data frame hakkinda bilgi edinelim
print(df.describe())
print("***************************************")

print(df.head())
print("***************************************")


# Bos degerler var mi ?, sonuc = yok 
print(df.isna())
print("***************************************")

# null deger var mi?, sonuc = yok
print(f"Null deger sayisi : {df.isnull().sum()}")
print("***************************************")

# duplicate eleman var mi? 
print(f"Duplicate elemanlar : {df.duplicated().sum()}")
print("***************************************")

# min max kalite 
print(f"Quality min : {df["quality"].min()}")
print(f"Quality max : {df["quality"].max()}")
print("***************************************")

# kalitelerdeki sarap sayisi
print(df["quality"].value_counts())
print("***************************************")

# bu sayilari basta dilimi olarak bastiralim
plt.figure()
df["quality"].value_counts().plot(kind = "pie")
plt.show()

# ya da bar olarak 
plt.figure()
df["quality"].value_counts().plot(kind = "bar")
plt.show()

# kalite dagilimina bakalim, sonuc = genel olarak alkol arttigi zaman kalite de artiyor, 5. kalitede cok outlier var 
plt.figure()
sns.set_style("whitegrid")
sns.boxplot(x = "quality", y = "alcohol", data = df)
plt.title("quality vs alcohol")
plt.xlabel("quality")
plt.ylabel("alcohol")
plt.show()

# kalite ph dagilimina bakalim, sonuc = ph ve kalite bagi icin kesin bir sey soylenemiyor
plt.figure()
sns.set_style("whitegrid")
sns.scatterplot(x = "quality", y = "pH", data = df)
plt.title("quality vs pH")
plt.xlabel("quality")
plt.ylabel("pH")
plt.show()

# kalite ve sitrik asit bakalim, sonuc = genel olarak dogru orantili bir sekilde gidiyor artarsa artar 
plt.figure()
sns.set_style("whitegrid")
sns.lineplot(x = "quality", y = "citric acid", data = df)
plt.title("quality vs citric acid")
plt.xlabel("quality")
plt.ylabel("citric acid")
plt.show()

# histogram bakalım, sonuc = genel olarak 5 ve 6. kalitede cok fazla veri var, 3. ve 8. kalitede cok az veri var 
plt.figure()
plt.hist(df["quality"])
plt.title("quality distribution")
plt.xlabel("quality")
plt.ylabel("frequency")
plt.show()

# seker ile kaliteye bakalim, genel olarak bir sey soylenemiyor ama 7 ve 8. kalitede genelde digerlerine gore seker yuksek
plt.figure()
sns.lineplot(x = "quality", y = "residual sugar", data = df)
plt.title("quality vs residual sugar")
plt.xlabel("quality")
plt.ylabel("residual sugar")
plt.show()

# 3 tane asit cesidinin kaliteyi nasil etkiledigine bakalim 
# asitlerle alakali sonuc = 8. kalitedeki saraplarda genel olarak asitler dusuk 
plt.figure()
plt.subplot(1,3,1)
sns.scatterplot(x = "quality", y = "citric acid", data = df)
plt.title("quality vs citric acid")
plt.xlabel("quality")
plt.ylabel("citric acid")
plt.tight_layout()
plt.subplot(1,3,2)
sns.scatterplot(x = "quality", y = "fixed acidity", data = df)
plt.title("quality vs fixed acidity")
plt.xlabel("quality")
plt.ylabel("fixed acidity")
plt.tight_layout()
plt.subplot(1,3,3)
sns.scatterplot(x = "quality", y = "volatile acidity", data = df)
plt.title("quality vs volatile acidity")
plt.xlabel("quality")
plt.ylabel("volatile acidity")
plt.tight_layout()
plt.show()

# kalitenin en cok volatile asit ile ters orantılı, en dogru orantili oldugu sey ise alkol 
# yogunlukla ph ve alkol ile ters orantili, ama asitlikle dogru orantili
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot = True) # deger ne kadar pozitif ve fazlaysa o kadar dogru orantili, ne kadar negatif ve azsa o kadar ters orantili
plt.show()


# kalitelere gore group by ve ortalamalari
print(df.groupby(["quality"]).mean())
print("***************************************")


# kaggle icin onemli 
columns = df.columns
(fig, ax) = plt.subplots(4,4, figsize = (16,15))
ax = ax.flatten()

for i, column in enumerate(columns):
    sns.kdeplot(
        data = df,
        x = column,
        hue = df.quality,
        ax = ax[i]
    )

# bos grafikleri siliyoruz
for i in range(i + 1, len(ax)):
    ax[i].axis("off")

    ax[i].set_title(f"{column} Distribution") 
    ax[i].set_xlabel(None) # x ile basliklar cakistigindan kaldirdik

plt.show()
print("***************************************")