# https://leetcode.com/problems/roman-to-integer/
"""
Notes:
"""

from problems.strings.roman_to_integer import Solution

class TestRomanToInteger:
    """
    Test Class
    """
    def test_one(self):
        """
        Test Case
        """
        assert Solution().romanToInt("III") == 3
        
    def test_two(self):
        """
        Test Case
        """
        assert Solution().romanToInt("IV") == 4
        
    def test_three(self):
        """
        Test Case
        """
        assert Solution().romanToInt("IX") == 9
        
    def test_four(self):
        """
        Test Case
        """
        assert Solution().romanToInt("LVIII") == 58
    
    def test_five(self):
        """
        Test Case
        """
        assert Solution().romanToInt("MCMXCIV") == 1994
        
    def test_six(self):
        """
        Test Case
        """
        assert Solution().romanToInt("MMMCMXCIX") == 3999