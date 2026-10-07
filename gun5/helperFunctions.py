
myList = list(range(10))
myList2 = list(range(5,20))
myList3 = list(range(5,20,2))
print(myList)
print(myList2)
print(myList3)

print("**************")

print("for loop started")
for element in enumerate(myList2): # tuple içinde indexler ve değerlerini veriyor
    print(element)
print("for loop ended")

print("**************")

print("for loop started")
for index,value in enumerate(myList2):
    print(f"Index: {index}, Value: {value}") # ayrı ayrı da alabiliriz
print("for loop ended")

print("**************")

from random import randint
print(randint(0,100))

from random import shuffle
myList4 = [1,2,3,4,5,6,7,8,9,10]
shuffle(myList4)
print(myList4)


print("**************")

foodList = ["Banana", "Apple", "Orange"]
calorieList = [100,200,300]
dayList = ["Monday","Tuesday","Wednesday"]

zippedList = zip(foodList,calorieList,dayList)
print(list(zippedList))

print("**************")

myString = "Batu"

newList = [element for element in myString]
print(newList)

print("**************")

numberList = [10,20,30,40]
newNumberList = [num/2 for num in numberList]
print(newNumberList)