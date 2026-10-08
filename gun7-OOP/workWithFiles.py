myFile = open("myfile.txt") # aynı dizinde olmasaydı /Users/batu/...../myfile.txt yazardık
print(type(myFile))
print(myFile.read())
print(myFile.read()) # boş okur çünkü okuma ucu en sona geldi boş yeri gösteriyor
myFile.seek(0) # okuma ucu en başa gider
print(myFile.read()) # yine okur
print(myFile.read()) # yine boş okur çünkü sona geldi

myFile.close() # dosya ile işimiz bittikten sonra kapatmalıyız

# baska yontem de var 
with open("myfile.txt") as myFile:
    myContent = myFile.read()

print(myContent) # artık istediğimiz kadar gösterebiliriz çünkü değişkene atadık 
                 # ama okuduktan sonra tekrar okutup değişkene atarsak boş döner
print(myContent)

# w -> write, r -> read, a -> append
print("*********************")
with open("myfile.txt", mode = "w") as myNewFile:
    myNewFile.write("test4") # içeriği komple test4 olarak değiştiriyor

with open("myfile.txt", mode = "r") as myFile2:
    myContent2 = myFile2.read()

print(myContent2)

with open("myfile.txt", mode = "a") as myFile3:
    myFile3.write("test5")

with open("myfile.txt", mode = "r") as myFile4:
    myContent3 = myFile4.read()

print(myContent3) # goreceğizki test4 ve test5 yan yana yazmış yani append eklemiş
                  