"""
https://leetcode.com/problems/top-k-frequent-elements/

Notes:
This algo is similar to bucket sort. The trick is to use a list index to our advantage.

1. Create a freq_list of length of the nums_list, let each index hold a empty list.
2. Since we know that k will be in range of 1 to k, we can use the list index from 1 to k.
3. Create a counter dict for the nums_list.
4. Loop through the counter dict items
5. Based on the count (value) in counter dict (mirror of index in freq_list), add the key to the internal list which 
is placed in freq_list at the same index as count (value).
6. initalize a result list.
7. Loop through the freq_list in reverse order, each element will be the internal list.
8. Loop through the internal list and append element to result list.
9. Once result lists length reaches k, break or return the result list.

Time: O(n)
"""
from typing import List
from collections import Counter



class Solution:
    def topKFrequent(self, nums_list: List[int], k: int) -> List[int]:
        freq_list = []
        counter = Counter(nums_list)
        freq_list = [list() for _ in range(len(nums_list)+1)]
        for key, value in counter.items():
            freq_list[value].append(key)
        result = []
        for i in range(len(freq_list)-1, 0, -1):
            for j in freq_list[i]:
                result.append(j)
                if len(result) == k:
                    return result



"""
# Alternate solution which is not space efficient
class Solution:
    def topKFrequent(self, nums_list: List[int], k: int) -> List[int]:
        result = []
        unsorted_counter = Counter(nums_list)
        counter = OrderedDict(sorted(unsorted_counter.items(), key=lambda x:x[1], reverse=True))
        result = [i for i in counter.keys()][:k]
        return result
        
# There is a solution with Heap which I need to learn.
"""