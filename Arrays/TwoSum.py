from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    comp = []

    for index, value in enumerate(nums):
        if value in comp:
            return [comp.index(value),index]
        comp.append(target-value)
