"""
Test Suite for the best_time_to_buy_and_sell_stock
"""
from problems.list.best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyStock:
    """
    Test Class
    """
    def test_one(self):
        nums = [7,1,5,3,6,4]
        expected = 5
        actual_max_sum = Solution().maxProfit(nums)
        assert actual_max_sum == expected
        
    def test_two(self):
        nums = [7,6,4,3,1]
        expected = 0
        actual_max_sum = Solution().maxProfit(nums)
        assert actual_max_sum == expected
        
    def test_three(self):
        nums = [1,2]
        expected = 1
        actual_max_sum = Solution().maxProfit(nums)
        assert actual_max_sum == expected
        
    def test_four(self):
        nums = [2, 6, 3, 10]
        expected = 8
        actual_max_sum = Solution().maxProfit(nums)
        assert actual_max_sum == expected
        
    def test_five(self):
        nums = [3, 6, 1, 5]
        expected = 4
        actual_max_sum = Solution().maxProfit(nums)
        assert actual_max_sum == expected