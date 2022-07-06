"""
# https://leetcode.com/problems/valid-anagram/

Notes:
1. First check if both strings are of same length
2. Create a counter dict for each of the string
3. Loop through first dict and check if the both dicts key has the different value
4. Return False if there is a key error
"""

class Solution:
    def isAnagram(self, str_one: str, str_two: str) -> bool:
        if len(str_one) != len(str_two):
            return False
        dict_one , dict_two = dict(), dict()
        for char in str_one:
            dict_one[char] = dict_one.get(char, 0) + 1
            
        for char in str_two:
            dict_two[char] = dict_two.get(char, 0) + 1
        for key in dict_one:
            try:
                if dict_one[key] != dict_two[key]:
                    return False
            except KeyError:
                return False
        return True
