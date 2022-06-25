'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        
        if len(s) != len(t):
            return False

        for i in s:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
        
        for i in t:
            if i in chars and chars[i]:
                chars[i] -= 1
            else:
                return False
        
        return True