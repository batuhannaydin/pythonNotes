# tipleri belirtme, sadece kod okunulabilirliği arttırıyor kullanmasan da olur 

name : str = "Batu"
print(type(name))

# bu genelde kullanılır ama üstteki cok kullanılmıyor 
def addNumbers(a: int, b: int) -> int: 
    return a + b

print(addNumbers(1,2))

print("******************")

# value hem int hem str olabilir 
def processValue(value: int | str) -> str:  
    if isinstance(value, int): # ifinstance, value'nun tipini kontrol eder 
        return f"Integer value: {value}"
    else: 
        return f"String value: {value}"

print(processValue(1))
print(processValue("a"))

print("******************")

from typing import List
def sumList(numbers: List[int]) -> int:
    return sum(numbers)

numbers = [1,2,3,4]
total = sumList(numbers)
print(total)