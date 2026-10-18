import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("athlete_events.csv")
print(data.describe())
print("******************************************************")

print(data.head())
print("******************************************************")

print(data.info())
print("******************************************************")

plt.scatter("Height", "Weight", data = data)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show()