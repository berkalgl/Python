#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined

from types import NoneType


def findFirstRecurringCharacter(arr):
    dictionary = {}

    for val in arr:
        if dictionary.get(val):
            return val
        else: 
            dictionary[val] = "true"
    
    return NoneType

print(findFirstRecurringCharacter([2,5,5,2,3,5,1,2,4]))