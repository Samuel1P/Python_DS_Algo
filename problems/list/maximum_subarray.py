"""
maximum-subarray
https://leetcode.com/problems/maximum-subarray/

Notes:
This is called as the Kadane Algorithm.
read the question first and understand the expected result which is the max sum.

1. Initalise two counters, max sum and curr sum. max sum will be the first element and curr sum will be zero.
2. Loop through the list
3. add the next element to curr_sum and check if it is bigger than max_sum, if it is...then set the max sum as curr_sum
4. If curr_sum is negative, make it as zero. this is because of two reasons. If the subsequent element is positive,
then there is no point in holding on to the previous chain of elements of sum since starting a new chain is a better deal.
If the subsequent element is negative, it will bring down your curr_sum further down.


Time: O(n)
"""
from typing import List


class Solution:
    def maxSubArray(self, num_list: List[int]) -> int:
        max_sum = num_list[0]
        curr_sum = 0
        for num in num_list:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = num + curr_sum
            if curr_sum > max_sum: # max_sum = max(curr_sum, max_sum)
                max_sum = curr_sum

        return max_sum
