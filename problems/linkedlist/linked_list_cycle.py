# https://leetcode.com/problems/linked-list-cycle/description/
"""
linked-list-cycle

Approach notes are user-authored.
Fill step-by-step explanation after you implement.

Time: O(?)
Space: O(?)
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import Node


class Solution:
    def has_loop(self, head: Optional[Node]) -> bool:
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

    # compatibility with LeetCode-style naming
    def hasCycle(self, head: Optional[Node]) -> bool:
        return self.has_loop(head)
