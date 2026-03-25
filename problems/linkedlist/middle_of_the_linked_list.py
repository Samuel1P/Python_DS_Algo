# https://leetcode.com/problems/middle-of-the-linked-list/
"""
middle-of-the-linked-list

Notes:
1. Obvious soln is to know the length of the linkedlist and then divide it by 2 and reach that node in the list but we have constraint not to count the length.
2. Take two pointers. Both start at the head and traverses towards the tail.
3. One travels one node at a time and other one moves two node at a time. The exit condition for odd length LL is when the faster moving one is exactly at the tail, meaning there is no node.next. For even length LL, the fast ptr will be beyond the tail.
4. By the speed at which they move, when fast pointer (2x speed) reaches the tail, the slow pointer will be half way (1x) and can be called as the middle node.
5. For even number LL, there will be two middle node, we pick the second node because that's where slow pointer is.


Time: O(n)
Space: O(1)
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


"""
Interview variant: returning the FIRST middle node for even-length lists

Change the loop condition from:
    while fast_ptr and fast_ptr.next:       → returns second middle (current)

To:
    while fast_ptr.next and fast_ptr.next.next:  → returns first middle

Example: 1 -> 2 -> 3 -> 4 -> 5 -> 6
  Current condition  → slow stops at 4 (second middle)
  Variant condition  → slow stops at 3 (first middle)

For odd-length lists, both conditions return the same node.

Trade-off:
  `while fast_ptr and fast_ptr.next`          → safe for empty list (fast_ptr checked first)
  `while fast_ptr.next and fast_ptr.next.next` → crashes on empty list since fast_ptr.next
                                                  is accessed before checking if fast_ptr exists.
                                                  Needs an early guard: if not head: return None
"""
