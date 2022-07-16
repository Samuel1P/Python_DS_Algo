"""
Test Suite for the maximum-subarray
"""
from problems.list.maximum_subarray import Solution


class TestMaximumSubarray:
    """
    Test Class
    """
    def test_one(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected = 6
        actual_max_sum = Solution().maxSubArray(nums)
        assert actual_max_sum == expected
        
    def test_two(self):
        nums = [5,4,-1,7,8]
        expected = 23
        actual_max_sum = Solution().maxSubArray(nums)
        assert actual_max_sum == expected
        
    def test_three(self):
        nums = [1]
        expected = 1
        actual_max_sum = Solution().maxSubArray(nums)
        assert actual_max_sum == expected
        
    def test_four(self):
        nums = [-3, -2, -3, -1]
        expected = -1
        actual_max_sum = Solution().maxSubArray(nums)
        assert actual_max_sum == expected