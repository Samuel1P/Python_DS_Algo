# https://leetcode.com/problems/roman-to-integer/
"""
Notes:
Aprroach one:
1. Create a dictionary to hold the roman values and a counter to hold the total
2. Loop through the string, check for index error by using the length of string and then check if the current value is less than the next value.
3. If it is, subtract the current value from the total. This is the special cases where small is before large.
4. If it is not, add the current value to the total. This is the normal case.
5. Return the total value

Approach two:
1. In step3, we substract the current value twice from the total. 
2. Then step4, we do add for all the values. so one of the adds from step3 gets negated in case it was a special case.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        sv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0
        for i in range(len(s)):
            if i+1 < len(s) and sv[s[i]] < sv[s[i+1]]:
                val -= (sv[s[i]])
            else:
                val += sv[s[i]]
        return val
    

class Solution2:
    def romanToInt(self, s: str) -> int:
        sv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0
        for i in range(len(s)):
            if i+1 < len(s) and sv[s[i]] < sv[s[i+1]]:
                val -= (2 * sv[s[i]])
            val += sv[s[i]]
        return val