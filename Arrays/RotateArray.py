from typing import List

class Solution:
    def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums = nums[len(nums):None:-1]
        nums[0:k] = nums[k-1:None:-1]
        nums[k:len(nums)] = nums[len(nums):k-1:-1]

        print(nums)


Solution.rotate([1,2,3,4,5,6,7],3)