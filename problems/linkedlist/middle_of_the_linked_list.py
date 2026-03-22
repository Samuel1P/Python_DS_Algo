# https://leetcode.com/problems/middle-of-the-linked-list/
"""
middle-of-the-linked-list

Approach notes are user-authored.
Fill step-by-step explanation after you implement.

Time: O(?)
Space: O(?)
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import Node

# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle_node(self, head: Optional[Node]) -> Optional[Node]:
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    # compatibility wrapper with LeetCode method naming
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        return self.find_middle_node(head)
