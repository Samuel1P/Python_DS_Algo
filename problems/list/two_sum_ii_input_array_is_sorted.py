"""
two_sum_ii_input_array_is_sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Notes:
we assume the list is sorted in ascending order.

1. create two pointers, one at left edge and one at right last.
2. check if the sum of values at both pointers equal to exp sum.
    a. if pointer val sum is > exp sum, move the right pointer to left value.
    b. if pointer val sum is < exp sum, move the left pointer to the right value.
3. return the values at pointer if their sum is equal to exp sum.
4. Make sure left pointer and right pointer don't cross eachother to avoid dupicate calcuation.
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
        