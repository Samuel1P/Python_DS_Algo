"""
Test Suite for the two sum problem
"""
import pytest
import random
from problems.hashmaps.two_sum import Solution


class TestTwoSum:
    """
    Test Class
    """

    def test_one(self):
        nums = [2,7,11,15]
        target = 9
        soln = Solution().twoSum(nums, target)
        assert [0, 1] == soln

    def test_two(self):
        nums = [3,2,4]
        target = 6
        soln = Solution().twoSum(nums, target)
        assert [1,2] == soln
        
    def test_three(self):
        nums = [3,3]
        target = 6
        soln = Solution().twoSum(nums, target)
        assert [0,1] == soln     
