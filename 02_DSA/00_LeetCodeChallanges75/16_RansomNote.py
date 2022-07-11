'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        
        for char in magazine:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in ransomNote:
            if char in chars and chars[char]:
                chars[char] -= 1
            else:
                return False
        return True
        