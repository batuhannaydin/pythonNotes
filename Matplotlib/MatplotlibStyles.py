import numpy as np 
import matplotlib.pyplot as plt 

data1 = np.linspace(0,10,20)
data2 = data1 ** 2

# plot(data1, data2, color = " istersek hex kodu veririrz istersek adini gireriz", alpha ile saydamlik)
myFigure, myAxes = plt.subplots()
myAxes.plot(data1, data1 + 2, color = "blue", linewidth = 1)
myAxes.plot(data1, data1 + 3, color = "yellow", linewidth = 4)
myAxes.plot(data1, data1 + 4, color = "#c85d09", linestyle = "-.")
myAxes.plot(data1, data1 + 5, color = "#c85d09", linestyle = ":")
myAxes.plot(data1, data1 + 6, color = "red", linestyle = "--")
myAxes.plot(data1, data1 + 7, color = "#000000", linestyle = "-", marker = "o", markersize = 4, markeredgecolor="red")
myAxes.plot(data1, data1 + 8, color = "#000000", linestyle = "-", marker = "+", markersize = 4)
plt.show()

# farkli grafik sekilleri 

# scatter
plt.scatter(data1, data2)
plt.show()

# histogram 
newArray = np.random.randint(0,100,50)
plt.hist(newArray)
plt.show()

# box plot
plt.boxplot(newArray) # ortalama, standart sapma vs gozukuyor
plt.show()