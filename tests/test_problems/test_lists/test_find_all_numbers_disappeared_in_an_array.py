
"""
Test Suite for the find-all-numbers-disappeared-in-an-array/
"""

from problems.list.find_all_numbers_disappeared_in_an_array import Solution



class TestDissappearedNumbersInList:
    """
    Test Class
    """

    def setup_class(self):
        self.missin_nums_list = Solution()
        
    def test_one(self):
        nums = [4,3,2,7,8,2,3,1]
        expected = [5,6]
        missin_nums_list = self.missin_nums_list.findDisappearedNumbers(nums)
        assert missin_nums_list == expected
        
    def test_two(self):
        nums = [1,1]
        expected = [2]
        missin_nums_list = self.missin_nums_list.findDisappearedNumbers(nums)
        assert missin_nums_list == expected