'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parentheses = { '{' : '}', '(' : ')', '[' : ']' }

        for char in s:
            if char in parentheses:
                stack.append(char)
            elif not stack or parentheses[stack.pop()] != char:
                return False
        
        return not stack
