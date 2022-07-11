'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
https://leetcode.com/problems/maximum-subarray/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maximum = curr
        for i in nums:
            curr = max(curr + i, i)
            maximum = max(maximum, curr)
        
        return maximum