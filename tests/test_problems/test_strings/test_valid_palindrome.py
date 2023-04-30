# https://leetcode.com/problems/valid-palindrome/
"""
Notes:
"""

from problems.strings.valid_palindrome import Solution

class TestValidPalindrome:
    """
    Test Class
    """
    def test_one(self):
        inp = "A man, a plan, a canal: Panama"
        outp = Solution().isPalindrome(inp)
        assert outp is True
        
    def test_two(self):
        inp = "malayalam"
        outp = Solution().isPalindrome(inp)
        assert outp is True
        
    def test_three(self):
        inp = " "
        outp = Solution().isPalindrome(inp)
        assert outp is True
    
    def test_four(self):
        inp = "Mr. Owl ate my metal worm"
        outp = Solution().isPalindrome(inp)    
        assert outp is True
    
    def test_five(self):
        inp = "Was it a car or a cat I saw?"
        outp = Solution().isPalindrome(inp)    
        assert outp is True
        
    def test_six(self):
        inp = "race a car"
        outp = Solution().isPalindrome(inp)
        assert outp is False