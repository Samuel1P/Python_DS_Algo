"""
merge-sorted-array
https://leetcode.com/problems/merge-sorted-array/

Notes:
The Solution expects you to store the merged (sorted) list in nums1.
The trick is using 3 pointers. Here's how the pointers are initalized..
    * nums1_index_pointer - This points to the last valid number in nums1 list. exclude the place holder zeroes.
    * nums2_index_pointer - Points to the last element in nums2 list.
    * nums1_last_index_pointer - Points to the last element in nums1 list. Included the placeholders. 

0. Create a while loop to run until nums1_index_pointer and nums2_index_pointer are non negative.
1. Compare element in nums1_index_pointer and nums2_index_pointer on which is bigger.
2. Bigger element is pushed to nums1 at index of nums1_last_index_pointer.
3. Decrement nums1_last_index_pointer and the pointer which won the comparison in # 1
4. One edge case: If nums2_index_pointer is non zero, nums2 still has some elements to be merged.
5. Run a while loop until nums2_index_pointer is non negative.
6. Push the nums2_index_pointer index elements in nums2 to nums1 list at index nums1_last_index_pointer.

Time: O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index_pointer = m - 1
        nums2_index_pointer = n - 1
        nums1_last_index_pointer = nums1_index_pointer + nums2_index_pointer + 1
        while nums1_index_pointer >= 0 and nums2_index_pointer >= 0:
            if nums1[nums1_index_pointer] < nums2[nums2_index_pointer]:
                nums1[nums1_last_index_pointer] = nums2[nums2_index_pointer]
                nums2_index_pointer -= 1
                nums1_last_index_pointer -= 1
            else:
                nums1[nums1_last_index_pointer] = nums1[nums1_index_pointer]
                nums1_index_pointer -= 1
                nums1_last_index_pointer -= 1
        while nums2_index_pointer >= 0:
            nums1[nums1_last_index_pointer] = nums2[nums2_index_pointer]
            nums1_last_index_pointer -= 1
            nums2_index_pointer-=1
