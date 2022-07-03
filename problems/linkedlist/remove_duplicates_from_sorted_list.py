
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Notes:
1. Take the first node in the first loop
2. In second loop, first check if there is a valid node next, if it there, check if that next nodes value is equal to current node.
3. If it is equal, then redirect current nodes dot next to the next nodes dot next node.
4. change the current node to next node

Time: Big O (n)
Space: O(1)

"""


class Solution:
    def deleteDuplicates(self, head):
        curr_node = head
        while curr_node:
            while curr_node.next and curr_node.value == curr_node.next.value:
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        return head
        
        