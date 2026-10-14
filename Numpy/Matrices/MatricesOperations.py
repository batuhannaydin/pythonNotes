import numpy as np 
newArray = np.random.randint(1,100,20) # 1 satırlık max 100 olacak sekilde 20 eleman
print(newArray)

print("*************************")

print(newArray > 50 ) # 50'den buyuk mu diye her elemani kontrol edip true veya false bastırır

print("*************************")

print(newArray[newArray > 50]) # kosulu saglayan elemanlari bastirir

print("*************************")

# transpose & reshape

matrixArray = np.array([[10,20], [20,30], [30,40]])
print(matrixArray)
print("*************************")
print(matrixArray.transpose()) # matrisi ters cevirir (satirlari sutun yapar)
# matrixArray.T ile de ayni seyi yapabiliriz 

print("*************************")

randomArray = np.random.random((6,1))
print(randomArray)

print("*************************")

# 6x1 lik matrixi 2x3 matrixe cevirelim
print(randomArray.reshape(2,3))

print("*************************")
# z-score ve outlier 
data = np.array([[10,12,13,15,18,25,100,105]])
mean = np.mean(data)
print(f"ortalama: {mean}")
std = np.std(data)
print(f"standart sapma: {std}")

zScore = (data-mean) / std
print(f"z score: {zScore}")

# outlierları alma 
print(data[zScore > 1]) # 100 ve 105 bastirir


# matematik denklem çözme 
# 2x + 3y = 8 and 5x + 7y = 19

# coefficient (katsayı) matrisi 
A = np.array([[2,3], [5,7]])

# constant matrisi 
b = np.array([8,19])

solution = np.linalg.solve(A,b)
print(f"çözüm: {solution}") # 1.0 ve 2.0 cevabını verir  x = 1 ve y = 2