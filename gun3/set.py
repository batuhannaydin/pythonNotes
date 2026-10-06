# tekrarlı eleman yok ve unordered bir liste gibi düşünebiliriz
myList = [10,20,10,30,40,20,40,50,60,30]
print(myList)

mySet = set(myList)
print(mySet)

mySet.add(50) # eklemeyecek çünkü 50 var
print(mySet)

myList2 = [30,40,50,60,70]
mySet2 = set(myList2)
print(mySet.union(mySet2))
print(mySet.intersection(mySet2)) # kesişim bulma
print(mySet.difference(mySet2)) # fark bulma mysetin 2den farkı 

print("***************************")
# boş set oluşturma 

emptySet = set()
print(emptySet)
print(type(emptySet))

emptySet.add(10)
emptySet.add(10)
emptySet.add(10)
emptySet.add(20)
emptySet.add(30)
print(emptySet)