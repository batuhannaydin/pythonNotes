class Fruit(): 
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories 

    # __str__ special method'dur, obje yazdırılmak istendiğinde çalışır
    def __str__(self): 
        return f"{self.name} ({self.calories} kcal)"

myFruit = Fruit("Banana:",120)
print(myFruit)


# python special methods diye aratırsak bulabiliriz