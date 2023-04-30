"""
# https://leetcode.com/problems/rotate-list/
Notes: 
Let's take an example..
length is = 5 , inp = 1,2,3,4,5, k=3
expected out = 3,4,5,1,2

step 1: pick the 4th item. that's your new new_head node (4).
step 2: pick 3rd item (3) and point to null. that's the new last node.
step 3: pick original tail (5) and point to old head (1)

1. if node is empty, return it
2. if node is alone, return it
3. take modulo of k with length of linked list to help with step 1 range calc and being efficient.
4. length_of_ll - k will move us to the 5 the item, since we are are at node(1) even before for loop starts. so we do -1.
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import Node, LinkedList
from data_structures.Linked_List.Doubly_Linked_List import DoublyLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[Node], k: int) -> Optional[Node]:
        if not head:
            return head
        length_of_ll = 1
        last_node_from_node = head
        while last_node_from_node.next:
            last_node_from_node = last_node_from_node.next
            length_of_ll +=1
        

        k = k % length_of_ll
        if k == 0:
            return head
        curr = head
        for _ in range(length_of_ll - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        last_node_from_node.next = head
        return new_head
    

class _Solution:
    """
    Local solution
    """
    def rotateRight(self, head: Optional[Node], k: int) -> Optional[Node]:
        if not head:
            return head
        length_of_ll = len(head)
        last_node_from_node = head
        while last_node_from_node.next:
            last_node_from_node = last_node_from_node.next

        k = k % length_of_ll
        if k == 0:
            return head
        curr = head
        for _ in range(length_of_ll - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        last_node_from_node.next = head
        return new_head
