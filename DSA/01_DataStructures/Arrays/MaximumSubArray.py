from typing import List

def maxSubArray(nums: List[int]) -> int:
    maxValue = nums[0]
    curr = maxValue
    for i in range(1, len(nums)):
        curr = max(curr + nums[i], nums[i])
        maxValue = max(curr, maxValue)
    
    return maxValue

print('Sum: ', maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
