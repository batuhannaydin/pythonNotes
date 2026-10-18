import numpy as np 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

# box plot 
data = np.array([5, 7, 9, 15, 20, 22, 25, 30, 32, 35, 37, 40, 50, 55, 60, 100])

# ortadaki cizgi medyan, alttaki cizgi min ustteki cizgi max en ustteki nokta outlier
# mavilikler de degerlerin hangi aralikta dagildigi yogunlastigi
plt.figure(figsize = (6,5))
sns.boxplot(y = data)
plt.title("Box Plot")
plt.ylabel("Data Value")
plt.grid(True)
plt.show()

# seaborn'un hazir datasetleri var ondan titanic'i cagiralim
df = sns.load_dataset("titanic")
print(df)
print("*************************")

plt.subplot(1,2,1)
sns.boxplot(x = "class", y = "age", data = df)
plt.title("Age by Class")
plt.xlabel("Class")
plt.ylabel("Age")

plt.subplot(1,2,2)
sns.boxplot(x = "class", y = "fare", data = df)
plt.title("Fare by Class")
plt.xlabel("Class")
plt.ylabel("Fare")
plt.show()