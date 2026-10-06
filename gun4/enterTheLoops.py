myList = [10, 16, 20, 30, 40, 50, 61]

print("for loop started")
for num in myList:
    print(num)
print("for loop ended")

print("************************")

print("for loop started")
for item in myList:
    new_num = item ** 2
    print(new_num)
print("for loop ended")

print("************************")

print("for loop started")
for number in myList:
    if number % 5 == 0:
        print(number)
print("for loop ended")

print("************************")

print("for loop started")
myString = "Batuhan Aydin"
for c in myString:
    print(c)
print("for loop ended")

print("************************")

# list içinde tuple
myNewList = [("a", "b"), ("c","d"), ("e","d")] 

for numm in myNewList:
    print(numm)

#tuple unpacking
for (x,y) in myNewList:
    print(x)