#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s: str) -> int:
    dictionary = {}
    for val in s:
        if dictionary.get(val):
            dictionary[val] += 1
        else:
            dictionary[val] = 1

    for idx,val in enumerate(s):
        if dictionary[val] == 1:
            return idx
    return -1


print(firstUniqChar("leetcode"))