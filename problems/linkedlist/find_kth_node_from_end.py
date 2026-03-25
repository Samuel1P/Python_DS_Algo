# https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
"""
find-kth-node-from-end

Notes:
1. It's a very clever soln. We create two pointers. move one (fast) pointer to k distance in the LL. Kind of offet. (if LL is not lengthy enough for the offset, we exit)
2. Now start moving both pointers one by one until the fast pointers becomes none.
3. slow pointer would be at the node which is k distance (the offset we set earlier)

Time: O(n)
Space: O(1)
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