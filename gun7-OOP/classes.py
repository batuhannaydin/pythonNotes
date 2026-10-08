# Büyük harflerle başlarlar

class Person():
    # name = ""   bunları yazmaya gerek yok 
    # age = 0
    # gender = ""
    
    # self sınıftaki değişkenlere referans veriyor. init, obje oluşturulurken çağırılıyor
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def printName(self):
        print(self.name) # normalde name değişkeni initte ama self ile o sınıfın name propertysine erişiyoruz

batuhan = Person("Batuhan",23,"Male")
print(batuhan.name, batuhan.age, batuhan.gender)
batuhan.printName()
print(type(batuhan))



