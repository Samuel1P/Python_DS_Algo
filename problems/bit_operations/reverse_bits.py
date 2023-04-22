"""
reverse-bits/
https://leetcode.com/problems/reverse-bits/

Notes: The actual problem is for 32 bit unsigned value but I have changed it to 4 bit for better understanding on what is happening.

Best way to undertand is to use num 10, pen and paper with debugger and follow each iteration.

> The number of iteration is equal to the bit length. Here 10 in binary is 1010, so we want to do 4 iteration.
> (num >> i) -> right shift removes the i number of places from binary value.
> (num >> i) & 1 -> &1 logic allows us to isolate the last bit. this is the bit that needs needs to pushed to the relative front.
> (bit << (3-i)) -> this allows to form the isolated bit in the relative place.
> res | (bit << (3-i)) -> res| logic allows the 1s to be pushed in to their relative place since exisiting place is occupied by default 0.

"""

class Solution:
    def reverseBits(self, num: int) -> int:
        res = 0
        for i in range(4):
            bit = (num >> i) & 1
            res = res | (bit << (3-i))
        return res

class _Solution:
    # Leetcode
    def reverseBits(self, num: int) -> int:
        res = 0
        for i in range(32):
            bit = (num >> i) & 1
            res = res | (bit << (31-i))
        return res
