class Dog():
    year = 7

    def __init__(self, age = 5): # age burda default 5 alınıyor değer verilmezse
        self.age = age
    
    def humanAge(self):
        return self.age * self.year # Dog.year da olur doğrudur

myDog = Dog(3)
humanAge = myDog.humanAge()
print(humanAge)