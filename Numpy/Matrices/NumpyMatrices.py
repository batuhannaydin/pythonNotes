import numpy as np 

# normal olarak matris oluşturma : 
# myMatrix = [[1,2], [3,4]]
# np.ones((3,2)) # 3 satırlı 2 kolonlu yani 3'e 2 bir matrix olusturulur

myNumpyMatrix = np.array([[5, 10], [15, 20]]) # 5 10 
print(myNumpyMatrix)                          # 15 20 seklinde bir matrix olusturulur 


print("*********************************")

# ilk yazılan row (satır) ikinci yazılan column (kolon)
print(myNumpyMatrix[1][0]) # 2. satır 1. eleman (15)
print(myNumpyMatrix[0][0]) # 1. satır 1. eleman 5 

print("*********************************")

# matrix elemanları toplamı 
print(myNumpyMatrix.sum()) # 5+10+15+20 = 50 

print("*********************************")

# 5'e 3'lük bir sıfırlardan olusan matrix yapalım 
myZerosMatrix = np.zeros((5,3))
print(myZerosMatrix)
 
print("*********************************")

# Matrix arithmetic

firstMatrix = np.array([[10, 20], [30, 40]])
secondMatrix = np.array([[5, 15], [25, 35]])

print(f"Matrixlerin toplamı: \n{firstMatrix + secondMatrix}")

print("*********************************")

# eger matrislerin boyutu aynı dgilse birisi tek boyutluysa, numpy bunu otomatik olarak matrise yayar 
thirdMatrix = np.array([[10, 20], [30, 40]])
FourthMatrix = np.array([[50, 60]])
print(thirdMatrix + FourthMatrix)

print("*********************************")

# 2 satır 1 kolonlu matrix olusturma 
fifthMatrix = np.array([[10], [20]]) # 2 satır 1 kolonlu matrix
print(fifthMatrix)

print("*********************************")

# Matrix boyutunu ogrenme
print(fifthMatrix.shape)

print("*********************************")

# Matrix Carpımı (multiplication)
# Carpım yapabilmek için ilk matrisin satır sayısı ile ikinci matrisin kolon sayısının eşit olması gerekir. 
# Yani 2x2 bir matris ile 2x3  = 2x3 bir matrisi çarpabiliriz  ya da 1x3 ile 3x2 = 1x2

print(firstMatrix * secondMatrix)

print("*********************************")

dataMatrix = np.array([[1, 2, 3]])
powersOfTenMatrix = np.array([[1, 10], [100, 1000], [10000, 100000]])

# yani 1x3 matrix ile 3x2 matrix carpimi olacak 
# 1 ile 1, 2 ile 100, 3 ile 10000 carpilip toplanacak ve 1x2lik olusacak matrixin ilk yerine yazılacak
# 1 ile 10, 2 ile 1000, 3 ile 100000 carpilip toplanacak ve 1x2lik olusacak matrixin ikinci yerine yazılacak 

print(np.dot(dataMatrix, powersOfTenMatrix))

print("*********************************")

# ya da 

print(dataMatrix.dot(powersOfTenMatrix))