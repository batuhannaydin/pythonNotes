class Musician():
    def __init__(self,name):
        self.name = name
        print("Musician class")

    def test1(self):
        print("test1")
    
    def test2(self):
        print("test2")

# miras alınacak sınıf parametre içine yazılır
class MusicianPlus(Musician):
    def __init__(self,name):
        Musician.__init__(self,name)
        print("Musician Plus")
    
    def test3(self):
        print("test3")

batu = MusicianPlus("Batu") # hem musician class hem de musician plus yazdırılır
batu.test1() # Musician sınıfındaki metotlara da erişebiliyor

# ama mesela musician plus olmayanlar test3 fonksiyonunu çalıştıramaz

# ama musician plusta test1 fonksiyonunu tekrar yazarsak override etmiş oluruz 
# o da sadece o sınıfta değişir kalıtım alınan yerde hala aynı 