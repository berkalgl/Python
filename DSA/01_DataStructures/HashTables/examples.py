dictionary = {
    "age" : 23,
    "name" : 'Berk',
    "magic" : True,
    "scream" : lambda x: print(x)
}

dictionary["age"]
print(dictionary["scream"]("Hello")) #O(1)

dictionary["spell"] = 'abra kadabra' #O(1)