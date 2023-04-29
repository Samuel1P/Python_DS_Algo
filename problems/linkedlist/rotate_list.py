# https://leetcode.com/problems/rotate-list/
"""
Notes: (rerite this)

Node('1') --points-to--> Node('2') --points-to--> Node('3') --points-to--> Node('4') --points-to--> Node('5') --points-to--> None
lenght is = 5
inp = 1,2,3,4,5
k=3
pick the 4th item. that's new_head
pick 3rd item and point to null
pick curr tail and connect to old head
make 3rd item the new_tail

ans = 3,4,5,1,2
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
