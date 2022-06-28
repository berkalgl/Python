'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
https://leetcode.com/problems/majority-element/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        source = {}
        
        for i in nums:
            if i in source and source[i]:
                source[i] += 1
            else:
                source[i] = 1
        
        for elem in source:
            if source[elem] > len(nums) / 2:
                return elem
            