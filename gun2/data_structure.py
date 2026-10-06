# indexing

myString = "Batuhan"
print(myString[0])
print(myString[6])
print(myString[-1]) # sondan ilk eleman

print("*******************************")

# Stringlerde toplama
name = "Batuhan"
surname = "Aydin"
sumString = name + " " + surname
print(sumString)

print(name * 5)
print("*******************************")

# Slicing. (starting index, stopping index, stepping size)
barcode = "ABCDE12345"
print(barcode[3::]) # 3. indexten başlar sonuna kadar gider
print(barcode[3::2]) # 3. indexten başlar sonuna kadar gider 2 atlayarak gider
print(barcode[1:9:2]) # 1. indexten başlar 7. indexe kadar gider 2 atlayarak gider
print(barcode[::-1]) # stringi tersine çevirir
print(barcode[:3:]) # 3. indexe kadar print eder

# index ile aradığımız harfin ilk hangi indexte olduğunu söyler
print(name.index("t")) 

# split ise verdiğin şeye göre böler bir şey vermezsek boşluğa göre böler
print(sumString.split())