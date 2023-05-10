
from problems.strings.longest_substring_without_repeating_chars import Solution

class TestLongestSubStringWithoutRepeatingChars:
    """
    Test Class
    """
    def test_one(self):
        inp = "abcabcbb"
        outp = Solution().lengthOfLongestSubstring(inp)
        assert outp == 3
        
    def test_two(self):
        inp = "bbbbb"
        outp = Solution().lengthOfLongestSubstring(inp)
        assert outp == 1
    
    def test_three(self):
        inp = "pwwkew"
        outp = Solution().lengthOfLongestSubstring(inp)
        assert outp == 3