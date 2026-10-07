# soyutlama da olarak adlandırılıyor, swiftteki protokolle aynı
# direkt sınıfı kullanmak yerine onun soyutunu kullanıyoruz

from abc import ABC, abstractmethod

class Car(ABC): # soyut sınıf, bundan obje oluşturulamaz genelde inheritance için kullanılır

    @abstractmethod # soyut metot
    def maxSpeed():
        pass 

class Tesla(Car):
    def maxSpeed(self):
        print("200km/h")

tesla = Tesla()
tesla.maxSpeed()

class Mercedes(Car):
    def maxSpeed(self):
        print("150km/h")


benz = Mercedes()
benz.maxSpeed()