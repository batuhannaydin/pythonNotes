import pandas as pd 
import seaborn as sns 
import matplotlib
matplotlib.use('TkAgg') # 
import matplotlib.pyplot as plt

data = pd.read_csv("../Matplotlib/athlete_events.csv")
print(data.describe())
print("*****************************")

print(data.info())
print("*****************************")

# 1. GRAFİK
plt.figure()
sns.set_style("whitegrid") 
sns.scatterplot(x = "Height", y = "Weight", data = data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show() # 

# 2. GRAFİK
# cinsiyete gore kilo'nun degisimi 
plt.figure()
sns.set_style("whitegrid") 
sns.scatterplot(x = "Height", y = "Weight", hue = "Sex", data = data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight by Sex")
plt.show() 

print(data.columns)
print(data["Medal"].unique()) 
print(data["Sex"].unique()) 

# 3. GRAFİK
# hem hue hem style kullanimi, renkleri cinsiyete gore stilleri madalyalara gore
plt.figure()
sns.set_style("whitegrid") 
sns.scatterplot(x = "Height", y = "Weight", hue = "Sex", style = "Medal", data = data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight by Sex and Medal")
plt.show() 

# 4. GRAFİK
# cizgi grafigi 
plt.figure()
sns.set_style("whitegrid") 
sns.lineplot(x = "Height", y = "Weight", hue = "Sex", data = data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight by Sex")
plt.show() 

# 5. GRAFİK

# sıklık grafigi 
plt.figure()
sns.set_style("white")
sns.displot(x = "Height",  hue = "Sex", data = data)
plt.ylabel("Frequency")
plt.title("Athletes Height Distrubition")
plt.show() 

# sıklık grafigi ama gosterimi cubuk degılde kopukluk olmadan dag gosterimi gibi
plt.figure()
sns.set_style("whitegrid")
sns.displot(x = "Height",  hue = "Sex", data = data, kind = "kde")
plt.ylabel("Frequency")
plt.title("Athletes Height Distrubition")
plt.show() 

# 6. GRAFİK
plt.figure()
sns.barplot(x = "Medal", y = "Height", hue = "Sex", data = data)
plt.title("Medals by Height")
plt.show()