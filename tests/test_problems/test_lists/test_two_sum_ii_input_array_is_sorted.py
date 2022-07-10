
"""
Test Suite for the two_sum_ii_input_array_is_sorted
"""
from problems.list.two_sum_ii_input_array_is_sorted import Solution


class TestTwoSum:
    """
    Test Class
    """
    def test_one(self):
        num_list = [2,7,11,15]
        target = 9
        actual_pair = Solution().twoSum(num_list, target)
        expected = [1,2]
        assert actual_pair == expected
        
    def test_two(self):
        num_list = [2,3,4]
        target = 6
        actual_pair = Solution().twoSum(num_list, target)
        expected = [1,3]
        assert actual_pair == expected
        
    def test_three(self):
        num_list = [-1,0]
        target = -1
        actual_pair = Solution().twoSum(num_list, target)
        expected = [1,2]
        assert actual_pair == expected