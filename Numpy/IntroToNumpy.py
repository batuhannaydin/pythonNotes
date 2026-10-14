import numpy as np 
myList = [10,20,30,40]

myNumpyArray = np.array(myList)
# ya da np.array([10,20,30,40]) ile de olusturabiliriz

print(type(myNumpyArray))
print(myNumpyArray)

print(f"maximum degeri: {myNumpyArray.max()}") # maximum degeri verir
print(f"minimum degeri: {myNumpyArray.min()}") # minimum degeri verir
print(f"medyan degeri: {myNumpyArray.mean()}") # ortalama degeri verir
print(f"standart sapma degeri: {myNumpyArray.std()}") # standart sapma degeri verir
print(f"toplam degeri: {myNumpyArray.sum()}") # toplam degeri verir
print(f"carpim degeri: {myNumpyArray.prod()}") # carpim degeri verir

print("******************")

print(np.zeros(3)) # 3 tane 0'li dizi
print(np.ones(3)) # 3 tane 1'li dizi
print(np.random.random(3)) # 3 tane rastgele sayili dizi

print("******************")

# listelerde aritmetik islemler
list1 = [10,20,30,40]
list2 = [50,60,70,80]
print(list1 + list2) # listeleri birlestirir

print("******************")

# numpy'da aritmetik islemler
myNumpyArray2 = np.array([1,2])
myNumpyArray3 = np.array([3,4])
print(myNumpyArray2 + myNumpyArray3) # degerleri toplar
print(myNumpyArray2 - myNumpyArray3)
print(myNumpyArray2 * myNumpyArray3)
print(myNumpyArray2 / myNumpyArray3)

print("******************")

# ya da 
print(myNumpyArray2 * 5)
print(myNumpyArray + 1) # her elemana 1 ekler 
#toplama carpma cıkarma bolme ıcın diziler esit boyutta olmalı veya birisi tek elemanlı olmalı

print("******************")

myNumpyArray4 = np.arange(0,10)
print(myNumpyArray4[1:4])