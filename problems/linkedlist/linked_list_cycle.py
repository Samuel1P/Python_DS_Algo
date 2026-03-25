# https://leetcode.com/problems/linked-list-cycle/description/
"""
linked-list-cycle

Notes:
1. Take two pointers. Both start at the head and traverses towards the tail.
2. One travels one node at a time and other one moves two node at a time.
3. the logic to know here is, the fast will max lapp the slow once. At some point before the slow ptr, laps its cycle loop , fast will catch slow.
4. Keep comparing nodes during every iteration. the exit condition is if fast pointer reaches None or fast pointer reaches past none or when slow ptr is same as fast ptr.

Time: O(n)
Space: O(1)
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
