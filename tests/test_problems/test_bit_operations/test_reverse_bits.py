"""
Test Suite for the reverse-bits problem
"""

from problems.bit_operations.reverse_bits import Solution


class TestReverseBits:
    """
    Test Class
    """
        
    def test_one(self):
        test_int = 0
        actual_result = Solution().reverseBits(test_int)
        assert actual_result == 0
        
    def test_two(self):
        test_int = 1
        actual_result = Solution().reverseBits(test_int)
        assert actual_result == 8

        
    def test_three(self):
        test_int = 10
        actual_result = Solution().reverseBits(test_int)
        assert actual_result == 5
        
        
    def test_four(self):
        test_int = 11
        actual_result = Solution().reverseBits(test_int)
        assert actual_result == 13
