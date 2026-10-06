# list ile benzer ama burda immutability var değiştirilemiyor

from importlib import machinery
myTuple = (10,"a","b",3.14)
print(type(myTuple))

print(myTuple[0])

# myTuple[0] = 20 

print(myTuple.count("a"))
print(myTuple.index("a"))