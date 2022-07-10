"""
two_sum_ii_input_array_is_sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Notes:

"""

from typing import List

class Solution:
    def twoSum(self, num_list: List[int], target: int) -> List[int]:
        left, right = 0, len(num_list) - 1
        while left < right:
            if num_list[left] + num_list[right] < target:
                left = left+1
            elif num_list[left] + num_list[right] > target:
                right = right-1
            elif num_list[left] + num_list[right] == target:
                return [left+1, right+1]
        