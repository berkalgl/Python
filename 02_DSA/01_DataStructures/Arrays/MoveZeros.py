from typing import List

def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insertedPosition = 0
        if nums.count(0) > 0:

            for i in nums:
                if i != 0: 
                    nums[insertedPosition] = i
                    insertedPosition += 1

            while insertedPosition < len(nums):
                nums[insertedPosition] = 0
                insertedPosition += 1


        