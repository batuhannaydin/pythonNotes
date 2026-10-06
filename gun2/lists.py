myList = [10,20,30,40,50]
print(myList[2])
print(myList)
myList[3] = 400
print(myList)
print(len(myList))
myList.append(60) # listeye eleman ekler
print(myList)
print(myList.index(60))
myList.remove(30) # listeden eleman siler
print(myList)
myList.pop() # listenin son elemanını siler
print(myList)
myList.pop(0) # listenin ilk elemanını siler
print(myList)
myList.insert(0,10) # listenin 0. indexine 10 ekler
print(myList)
myList.count(10) # 10'un kaç tane olduğunu söyler
print(myList)
myList.reverse() # listeyi ters çevirir
print(myList)
myList.sort() # listeyi sıralar
print(myList)
myList.clear() # listeyi boşaltır
print(myList)
print("*************************")

# x = input("Bir metin girin: ") ibput ile girdi alabiliyoruz ama bunlar hep string olarak geliyor isterse kullanıcı 10 yazsın
# veri tipi dönüştürme
myInteger1 = 10
print(type(str(myInteger1))) # str olarak karsımıza cıkar

myString = "10"
print(type(int(myString))) # int olarak karsımıza cıkar
print(float(myString))

print("*************************")

list1 = [1,2]
list2 = [3,4]
list3 = list1 + list2
print(list3)

print("*************************")

# nestedList
myNestedList = [1,[2,3],4,5]
print(myNestedList[1])
print(myNestedList[1][0]) # 2
