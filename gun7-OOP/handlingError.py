# yanlış tipte girdi girilebilir, veri gelmeyebilir veya beklenilebilir vb vb 

while True:
    try: 
        age = int(input("enter age: "))
        print(age)
        break # break yazmazsak sonsuz döngü
    except: # except ValueError: falan da diyebiliriz baska error tipleri de var
        print("Invalid value!")

