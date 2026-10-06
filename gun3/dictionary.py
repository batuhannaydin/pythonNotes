#key - value pairing

import mypy_extensions
fitness_dictionary = {"banana": 100, "orange": 150}
print(type(fitness_dictionary))
print(fitness_dictionary["banana"])
print(type(fitness_dictionary["banana"]))

print("***************************")

print(fitness_dictionary.keys()) # Sadece key'leri yazdırır
print(fitness_dictionary.values()) # Sadece value'leri yazdırır

#bunların tipleri string veya int değil dict keys ve dict value olarak gözükür bunları listeye alabiliriz
print(type(fitness_dictionary.keys())) # dict_keys türünde yazdırır
print(type(fitness_dictionary.values())) # dict_values türünde yazdırır

print(list(fitness_dictionary.keys())) # liste olarak yazdırır
print(type(list(fitness_dictionary.keys()))) # liste olarak yazdırır

print("***************************")

#dictionaryde value değiştirme
fitness_dictionary["banana"] = 300
print(fitness_dictionary)

#dictionarye yeni bir key ekleme
fitness_dictionary["apple"] = 100
print(fitness_dictionary)

#dictionaryden bir key-value silme
del fitness_dictionary["banana"]
print(fitness_dictionary)

# key value tipleri fark etmiyor str str int int str int hiç fark etmez 

my_mixed_dictionary = {"k1": 10, "k2": [10,20,30,40,50], "k3": "string", "k4": {"a":100, "b":200}}
print(my_mixed_dictionary["k4"]["b"])
print(my_mixed_dictionary["k2"][3])

# boş dictionary açma
emptyDictionary = dict() # veya = {}
print(emptyDictionary)
print(type(emptyDictionary))

emptyDictionary["key1"] = "value1"
emptyDictionary["key2"] = 20
print(emptyDictionary)
