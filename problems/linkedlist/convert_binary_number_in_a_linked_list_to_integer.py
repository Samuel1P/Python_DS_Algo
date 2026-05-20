# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""
convert-binary-number-in-a-linked-list-to-integer
Notes:
1. The head of the list is the MOST significant bit - we read bits left to right.
2. Trick: think of it like typing a number into a calculator one digit at a time.
   Every time you press a new digit, the existing digits "slide one place to the left",
   and the new digit drops into the now-empty ones place.
3. In base 10, sliding left = multiplying by 10.
   In base  2, sliding left = multiplying by 2.
4. Formula (works for any base):
       num = (num * base) + digit
   Typing 501 on a calculator (base 10):
       start   : num = 0
       press 5 : num = 0  * 10 + 5 = 5
       press 0 : num = 5  * 10 + 0 = 50
       press 1 : num = 50 * 10 + 1 = 501
   Walking the linked list [1, 0, 1] (base 2):
       start   : num = 0
       see 1   : num = 0 * 2 + 1 = 1    (binary: 1)
       see 0   : num = 1 * 2 + 0 = 2    (binary: 10)
       see 1   : num = 2 * 2 + 1 = 5    (binary: 101)
Time: O(n)   - single pass through the list
Space: O(1)  - only one accumulator variable
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import Node


class Solution:
    def getDecimalValue(self, head: Optional[Node]) -> int:
        temp = head
        num = 0
        while temp:
            num = (num * 2) + temp.val
            temp = temp.next
        return num
