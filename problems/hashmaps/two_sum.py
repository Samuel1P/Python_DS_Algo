# https://leetcode.com/problems/two-sum/
"""
Notes:
The problem expects only one pair. 
The solution is as follows:
1. initate a empty dictionary
2. loop through the input list, substract each element value with target and see if that result is present in dict from step 1. 
3. If it is not present, add it to the dict as {element_value: element_index}
4. If it is present in dict, return a list with [results value in dict (ele index),  loop_index]
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            if target - nums[i] in ref:
                return [ref[target-nums[i]], i]
            else:
                ref.update({nums[i]:i})

