import numpy as np 
import pandas as pd 

# random seed 

np.random.seed(42) # genelde 42 verilir

set1no = 900 
set2no = 100 

df1 = pd.DataFrame({
    "feature_1": np.random.normal(loc = 0, scale = 1, size = set1no),
    "feature_2": np.random.normal(loc = 0, scale = 1, size = set1no),
    "target": [0] * set1no
})

df2 = pd.DataFrame({
    "feature_1": np.random.normal(loc = 0, scale = 1, size = set2no),
    "feature_2": np.random.normal(loc = 0, scale = 1, size = set2no),
    "target": [1] * set2no
})

print(df1.head())
print("****************************")
print(df2.head())

# concat 
df = pd.concat([df1, df2]).reset_index(drop = True)

print("*******************COMBINED DATASET*******************")
print(df)

print("*****************Target Unique***********************")
print(df["target"].unique())

print("*******************VALUE COUNTS*******************")
print(df["target"].value_counts())



# upsampling -> upsample minortiy, az olani cogaltmak
# downsampling -> downsample majority, cok olani azaltmak

# minority yaptık az olani cogalttik
dfMinority = df[df["target"] == 1]
print("*******************MINORITY*******************")
print(dfMinority)

dfMajority = df[df["target"] == 0]
print("*******************MAJORITY*******************")
print(dfMajority)

from sklearn.utils import resample # resample -> sample boyutunu azalt veya arttir
dfMinorityUpsampled = resample(dfMinority, replace=True, n_samples=len(dfMajority), random_state=42)
print("*******************MINORITY UPSAMPLED*******************")
print(dfMinorityUpsampled)
print("*******************MINORITY UPSAMPLED SHAPE*******************")
print(dfMinorityUpsampled.shape)

# simdi concat yapalim bakalim kac satir
dfUpsampledConcat = pd.concat([dfMajority, dfMinorityUpsampled]).reset_index(drop = True)
print("*******************UPSAMPLED CONCAT*******************")
print(dfUpsampledConcat)
print("*******************UPSAMPLED CONCAT SHAPE*******************")
print(dfUpsampledConcat.shape)
print("*******************UPSAMPLED CONCAT VALUE COUNTS*******************")
print(dfUpsampledConcat["target"].value_counts())


# simdi de majority yapalım cogunlugu azaltalim

dfMajorityDownsampled = resample(dfMajority, replace=True, n_samples=len(dfMinority), random_state=42)
print("*******************MAJORITY DOWNSAMPLED*******************")
print(dfMajorityDownsampled["target"].value_counts())

dfDownsampledConcat = pd.concat([dfMajorityDownsampled, dfMinority]).reset_index(drop=True)
print("*******************DOWNSAMPLED CONCAT*******************")
print(dfDownsampledConcat["target"].value_counts())
print("*******************DOWNSAMPLED CONCAT SHAPE*******************")
print(dfDownsampledConcat.shape)

# ama genelde bunlar mantiksiz oluyor, daha mantıklısı var 
# SMOTE(Synthetic Minority Oversampling Technique)
# 900 tane 0, 100 tane 1 var az olan 1. 100 tane 1 yerine 900 tane 1 uretilecek ama benzer olcak duplicate degil 

import matplotlib.pyplot as plt 
plt.scatter(df["feature_1"], df["feature_2"], c = df["target"]) # c = renk
plt.show()
from imblearn.over_sampling import SMOTE
overSample = SMOTE()
(X,y) = overSample.fit_resample(df[["feature_1", "feature_2"]], df["target"]) # x feature, y target
overSampleDf = pd.concat([X,y], axis = 1)
print("------COGALTİLMİS------")
print(overSampleDf["target"].value_counts())


plt.scatter(overSampleDf["feature_1"], overSampleDf["feature_2"], c = overSampleDf["target"]) # c = renk
plt.show()

 