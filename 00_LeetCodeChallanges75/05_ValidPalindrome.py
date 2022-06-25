'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

https://leetcode.com/problems/valid-palindrome/
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)

        while end > start:
            if not s[start].isalnum():
                start += 1
            elif not s[end-1].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end-1].lower():
                    return False
                else:
                    start += 1
                    end -= 1

        return True

print(Solution.isPalindrome(None,"A man, a plan, a canal: Panama"))