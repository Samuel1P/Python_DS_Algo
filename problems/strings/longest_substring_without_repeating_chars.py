# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
Notes:
Brute force approach is to check every single substring but it is not optimal.
Optimal was is to solve it like window sliding problem.
1. create a set since set lookup is O(1) and it allows for checking duplicates.
2. create a pointer for index 0. create a result var that will hold the length of longest substring without repeating char.
3. Loop through the string with the loops index being right pointer.
4. if ele at right pointer is already in set, then remove the elements from left side using left pointer until that duplicate is removed. increment left pointer after each while loop to move it to the right side.
5. once the duplicate of right pointer ele is removed, add the right pointer ele to the set.
6. the result will be the max between exisiting result and the right to left distance.
"""

class Solution:
    # cabcabab
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        result = 0
        left_p = 0
        for right_p in range(len(s)):
            while s[right_p] in char_set:
                char_set.remove(s[left_p])
                left_p+=1
            char_set.add(s[right_p])
            result = max(result, right_p - left_p + 1)
        return result