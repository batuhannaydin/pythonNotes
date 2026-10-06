print(type(10)) # integer
print(type(1.4)) # float
print(type("a")) # string
print(type("hello world")) # string
print(type(True)) # boolean
print(type(False)) # boolean
print(type(None)) # none
print("***********************")
# variable
myfloat = 1.32345534
print(myfloat)
print(type(myfloat))
print("my name is Batu")
print("***********************")
# işin içinde float varsa sonuç floattır, bölü işlemlerinde full float
print(4-2) # integer
print(4.0 - 2) # float
print(4 / 2) # float
print("***********************")
# işlemler
print(2 * 5)
print(2 ** 5) # 2 üssü 5 
print(10 % 2) # 10un 2ye bölümünden kalan 

print("***********************")
# String
name = "batuhan"
print(type(name))
print(name.capitalize())

# String methotları 

print(name.count("a")) # name'in içinde kaç tane a var
print(name.upper()) # hepsini büyük yapar
print(len(name)) # uzunlugunu verir
print("batuhan \nAydin") # \n ile alt satıra geçiriyor \t ise tab yapar boşluk bırakır