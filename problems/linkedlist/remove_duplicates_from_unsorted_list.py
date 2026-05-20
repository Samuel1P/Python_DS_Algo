"""
https://www.geeksforgeeks.org/dsa/remove-duplicates-from-an-unsorted-linked-list/

Notes:
1. Method 1 using set.
2. Create a empty set to keep unique elements in a LL
3. Create two pointer, one for prev node and one for curr node.
4. At the start, prev will be none and curr will be head. 
5. Loop through the nodes using curr pointer, check if node value is in set, if not, add it to the set.
6. If it is present, link the prev node with curr.next node.

. Time: O(n)
. Space: O(n)
"""
from typing import Optional
from data_structures.Linked_List.Linked_List import Node


class Solution1:
    def removeDuplicates(self, head: Optional[Node]) -> None:
        unique_items = set()
        prev = None
        curr = head
        while curr:
            if curr.val not in unique_items:
                unique_items.add(curr.val)
                prev=curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr= curr.next

    def print_ll_data(self, head):
        self.removeDuplicates(head)
        curr = head
        while curr:
            print(curr.val, end=" ")
            curr= curr.next
        print()





class Solution2:
    """
    https://www.geeksforgeeks.org/dsa/remove-duplicates-from-an-unsorted-linked-list/

    Notes:
    1. This method uses nested loops
    2. create a curr pointer pointing to head and runner pointer inside the outer loop pointing to head node. 
    3. In the inner loop, compare the curr value with next nodes value which is runner.next
    4. if they are not the same, move the runner pointer to next node and continue the inner loop.
    5. If they are the same, make runners next as runner next next. 
    6. when runner reaches the end, we exit inner loop, move curr to next node in outer loop and make runner back to curr and enter inner loop again.
    . Time: O(n2)
    . Space: O(1)
    """
    def removeDuplicates(self, head: Optional[Node]) -> None:
        curr = head
        while curr:
            runner = curr
            while runner.next:
                if curr.val == runner.next.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            curr = curr.next
        
    
    def print_ll_data(self, head):
        self.removeDuplicates(head)
        curr = head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()