"""
find-all-numbers-disappeared-in-an-array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Notes:
1. The trick is to use the input list (num_list) to our advantage. 
2. Loop through num_list. for every number, use the number as an index and convert the value at that index to negative value.
3. This above logic makes sure only the index which are negative, are the only elements in num_list.
5. account for the index zero and the num_list starting at 1 and we are golden.
"""



class Solution:
    def findDisappearedNumbers(self, num_list):
        for number in num_list:
            index_to_neg = abs(number) - 1
            num_list[index_to_neg] = -1 * abs(num_list[index_to_neg])
        
        result = []
        for index, number in enumerate(num_list):
            if number > 0:
                result.append(index+1)
        return result
                