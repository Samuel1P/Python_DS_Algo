"""
3sum
https://leetcode.com/problems/3sum/

Notes:
1. sort the list.
2. for non first index nums (a), we check if prev element is same, if so..we skip it. since we can't have duplicate triads.
3. now do the two sum ii logic for b and c elements.
4. At the end, check if next b same as current b, if they are the same, skip ahead so we don't do duplicate calculation and end up adding dup pair.
"""

from typing import List

class Solution:
    def threeSum(self, num_list: List[int]) -> List[List[int]]:
        k = 0
        num_list.sort()
        output_ls = list()
        for index, num in enumerate(num_list):
            if index>0 and num == num_list[index-1]:
                continue
            left_p, right_p = index+1, len(num_list)-1
            while left_p < right_p:
                if (num + num_list[left_p] + num_list[right_p]) > k:
                    right_p -= 1
                elif (num + num_list[left_p] + num_list[right_p]) < k:
                    left_p += 1
                else:
                    output_ls.append([num, num_list[left_p], num_list[right_p]])
                    left_p += 1
                    while num_list[left_p] == num_list[left_p-1] and left_p < right_p:
                        left_p += 1
        return output_ls