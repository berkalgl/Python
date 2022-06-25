#https://leetcode.com/problems/two-sum/

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''

        #optimized solution
        sum = []
        for idx, value in enumerate(nums):
            if value in sum:
                return [sum.index(value), idx]
            sum.append(target - value)
            
