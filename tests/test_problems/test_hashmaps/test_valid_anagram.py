"""
Test Suite for the valid anagram
"""
from problems.hashmaps.valid_anagram import Solution


class TestValidAnagram:
    """
    Test Class
    """

    def test_one(self):
        str_one =  "anagram"
        str_two = "nagaram"
        assert Solution().isAnagram(str_one, str_two)

    def test_two(self):
        str_one =  "rat"
        str_two = "car"
        assert not Solution().isAnagram(str_one, str_two)
