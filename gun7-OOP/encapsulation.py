class Phone():
    def __init__(self,name,price):
        self.name = name 
        self.__price = price 
    
    def info(self):
        print(f"{self.name} price is: {self.__price}")

    def changePrice(self,price):
        self.__price = price # zaten sınıfın içinde oldugumuzdan erişebiliyoruz ondan __price yaptık 
# başına __ koyarsak onu private yapıyoruz

iphone = Phone("Iphone",10000)
# iphone.price yapamayız ama iphone.changePrice(100) dersek değiştirebiliriz veya çağırabiliriz 