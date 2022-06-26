'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result, freq = 0, sorted([s.count(i) for i in set(s)])
        for i in freq:
            if i % 2 == 0:
                result += i
            else:
                if result % 2 == 0:
                    result += 1
                result += i -1
        return result