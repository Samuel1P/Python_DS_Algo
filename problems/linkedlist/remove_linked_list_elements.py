
"""
https://leetcode.com/problems/remove-linked-list-elements/

Notes:

1. Initialize dummy node to avoid edge cases.
2. Create two pointers prev_node and curr_node.
3. prev_node will start as the dummy node and the curr_node will be the head.
4. Loop until curr_node is exhausted.
4.1 If curr node value is equal to target, connect prev node to next node from curr_node perspective.
4.2 If not, move prev_node to curr_node
5. move curr_node to next node.
6. return the next node form dummy node.

Space: O(1)
Time: O(n)

"""
from data_structures.Linked_List.Linked_List import Node


class Solution:
    def removeElements(self, head:Node, val):
        dummy_node = Node()
        prev_node = dummy_node
        curr_node = head
        dummy_node.next = curr_node
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return dummy_node.next
        
        