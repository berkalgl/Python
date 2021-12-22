from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    dict = {}
    for i in nums:
        if dict.get(i):
            return True
        else:
            dict[i] = True
    
    return False

print('Result: ', containsDuplicate([1,1,1,3,3,4,3,2,4,2]))