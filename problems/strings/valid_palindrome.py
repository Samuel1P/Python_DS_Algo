# https://leetcode.com/problems/valid-palindrome/
"""
Notes:
Aprroach one:
self explanatory but won't work for interviews.

Approach two:
1. Create a help method to check for alnum
2. create a left and right pointer
3. Loop the pointers until lp is less than rp
4. 
"""

class Solution:
    def _isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str+=char.lower()
        return new_str == new_str[::-1]
    
    def is_alnum(self, char):
        print((("a" <= char.lower() <= "z") or ("0" <= char.lower() <= "9")),char)
        return (("a" <= char.lower() <= "z") or ("0" <= char.lower() <= "9"))
        
    def isPalindrome(self, s: str) -> bool:
        left_p , right_p = 0, len(s) - 1
        while left_p < right_p:
            while left_p < right_p and not self.is_alnum(s[left_p]):
                left_p += 1
            while right_p > left_p and not self.is_alnum(s[right_p]):
                right_p -= 1
            if s[left_p].lower() != s[right_p].lower():
                return False
            left_p +=1
            right_p -= 1
        return True
            
