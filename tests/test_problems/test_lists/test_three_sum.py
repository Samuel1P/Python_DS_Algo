
"""
Test Suite for the two_sum_ii_input_array_is_sorted
"""
from problems.list.three_sum import Solution


class TestThreeSum:
    """
    Test Class
    """
    def test_one(self):
        num_list = [-1,0,1,2,-1,-4]
        actual_triad = Solution().threeSum(num_list)
        expected = [[-1,-1,2],[-1,0,1]]
        assert actual_triad == expected
        
    def test_two(self):
        num_list = [0,1,1]
        actual_triad = Solution().threeSum(num_list)
        expected = []
        assert actual_triad == expected
        
    def test_three(self):
        num_list = [0,0,0]
        actual_triad = Solution().threeSum(num_list)
        expected = [[0,0,0]]
        assert actual_triad == expected
        
    def test_four(self):
        num_list = [0,2,-2,3,-3]
        actual_triad = Solution().threeSum(num_list)
        expected = [[-3, 0, 3], [-2, 0, 2]]
        assert actual_triad == expected