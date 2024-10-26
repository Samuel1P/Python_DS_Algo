"""
# https://leetcode.com/problems/reverse-linked-list/description/
Notes:
Imagine this with a linked list of Void::1->2->3->None

1. Create two pointers prev and curr. prev will be None and curr will be head.
Void is now None and curr is 1.
2. 1.next is 2. So, we need to reverse the link. 
- 1.next to Void which is now None
- move prev to 1.
- move curr to 2.
3. eventually 3 will be curr and 2 will be prev.
- 3.next is none. So, we need to reverse the link.
- 3.next to 2
-  move prev to 3
-  move curr to curr.next which is None.
4. None is empty, loop ends. return prev which is now 3 and also the first node.
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import Node

# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev