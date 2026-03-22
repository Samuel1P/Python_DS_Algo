# https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
"""
find-kth-node-from-end

Approach notes are user-authored.
Fill step-by-step explanation after you implement.

Time: O(?)
Space: O(?)
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import LinkedList, Node


def find_kth_from_end_udemy(ll: LinkedList, k: int) -> Optional[Node]:
    """
    Return the kth node from the end of the linked list
    without using the length of the list.

    """
    
    slow_ptr, fast_ptr = ll.head, ll.head
    for _ in range(k):
        if not fast_ptr:
            return None
        fast_ptr = fast_ptr.next

    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr

def find_kth_from_end(ll: LinkedList, k: int) -> Optional[Node]:
    """
    Return the kth node from the end of the linked list
    without using the length of the list.

    """
    
    slow_ptr, fast_ptr = ll.head, ll.head
    for _ in range(k):
        if not fast_ptr:
            return -1
        fast_ptr = fast_ptr.next

    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr.val        