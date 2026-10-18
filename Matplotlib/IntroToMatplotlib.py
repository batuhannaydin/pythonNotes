import numpy as np
import matplotlib.pyplot as plt 

ageList = [10,20,30,30,30,40,60,70,75]
weightList = [20,60,80,85,86,87,70,90,95]


plt.plot(ageList, weightList, "y") # y-> yellow, b-> blue, g-> green, r-> red
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")
plt.show() # gosterebilmek icin bellege kaydedilen grafigi gosterebilmek lazim

# plt.savefig("test.png") ile grafigi dosya dizinine kaydedebiliyoruz


# numpy ile calistirma, usttekiyle ayni
npAgeList = np.array(ageList)
npWeightList = np.array(weightList)

plt.plot(npAgeList, npWeightList, "g")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")
plt.show()

numpyArray1 = np.linspace(0,10,20) # 0 ile 10 arasinda 20 sayi uretir esit aralikla
print(numpyArray1)
numpyArray2 = numpyArray1 ** 2

plt.plot(numpyArray1,numpyArray2, "b-*") # ilk'i x ekseni digeri y ekseni b* de olur b- de olur b--
plt.show()


# Eksenler, 2 tane grafik yan yana bastırılıyor
plt.subplot(1,2,1) # 1 row 2 column 1. grafik
plt.plot(numpyArray1, numpyArray2, "r*-")
plt.subplot(1,2,2) # 1 row 2 column 2. grafik
plt.plot(numpyArray2, numpyArray1, "g--")
plt.show()

# figure 
myFigure = plt.figure()
figureAxes = myFigure.add_axes([0.1,0.1,0.3,0.3]) # grafigin boyutlari
figureAxes.plot(numpyArray1, numpyArray2, "g")
figureAxes.set_xlabel("X Axis")
figureAxes.set_ylabel("Y Axis")
figureAxes.set_title("My Graph")
plt.show()

newFigure = plt.figure(dpi = 100) # ekran kalitesi, piksel sayisi
newAxes = newFigure.add_axes([0.1,0.1,0.9,0.9])
newAxes.plot(numpyArray1, numpyArray1 ** 2, label = "numpy array ** 2")
newAxes.plot(numpyArray1, numpyArray1 ** 3, label = "numpy array ** 3")
newAxes.legend() # label ismini gozukur yapar, sol ustte gozukuyor simdi
plt.show()