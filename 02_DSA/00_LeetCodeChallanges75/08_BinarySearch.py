'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/binary-search/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            
            middle = (start + end) // 2
            
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle -1
                
        return -1

    def searchRecursive(self, nums: List[int], start, end, target: int) -> int:
        if not len(nums) or start < end:
            return -1

        middle = start + (end - start) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            self.searchRecursive(nums, middle + 1, end, target)
        else:
            self.searchRecursive(nums, start, middle -1, target)