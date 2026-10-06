# Continue - Break - Past

myList = [10,20,30,40,50,60]

print("for loop started")
for num in myList:
    print(num)
    if num == 40:
        print("Deger bulundu donguden cıkılıyor")
        break
print("for loop ended")

print("********************")

print("for loop started")
for num1 in myList:
    if num1 == 40:
       continue # for icindeki alttaki kodları calıstırtmaz yani forda basa geçirtiyor
    print(num1)
print("for loop ended")

print("******************")

for num2 in myList:
    pass # for'u simdilik bos bırakiyoruz hata vermesini de istemiyoruz ondan bos bırakılıyor.