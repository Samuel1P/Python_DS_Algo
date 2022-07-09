"""
Test Suite for thetop_k_frequent_elements_hashmap
"""

from problems.hashmaps.top_k_frequent_elements_hashmap import Solution


class TesttopKFrequent:
    """
    Test Class
    """

    def test_one(self):
        nums_list = [1,1,1,2,2,3]
        k = 2
        expected = [1,2]
        soln = Solution().topKFrequent(nums_list, k)
        assert expected == soln

    def test_two(self):
        nums_list = [1]
        k = 1
        expected = [1]
        soln = Solution().topKFrequent(nums_list, k)
        assert expected == soln


    def test_three(self):
        nums_list = [4, 4, 5, 2, 4, 1, 1, 1, 1, 5, 1]
        k = 3
        expected = [1, 4, 5]
        soln = Solution().topKFrequent(nums_list, k)
        assert expected == soln