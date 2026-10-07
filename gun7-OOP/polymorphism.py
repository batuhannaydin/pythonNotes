class Banana():
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"100 calories {self.name}"

class Apple():
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"150 calories {self.name}"

# info metotları scope olarak sadece o sınıfa aitler ama adları aynı 
banana = Banana("Banana")
apple = Apple("Apple")

fruitList = [banana,apple]

# fruit bir banana oluyor bi apple ve ordaki farklı ama adı aynı olan info metodunu çağırıyor bu polymorphism
for fruit in fruitList:
    print(fruit.info()) 