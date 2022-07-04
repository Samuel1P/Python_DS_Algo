"""
merge-two-sorted-lists
https://leetcode.com/problems/merge-two-sorted-lists/

Notes:
You are getting head nodes of two linked list. both linked list are sorted. Neetcode guys is suggesting to use
a dummy node at the start to overcome some edge cases. not exactly sure what he means by that. For now, I'm simply dollowing it.

1.  Create a dummy node and call it tail
2. Loop through both linked list as long as both have some value.
3. Inside loop, compare the value of nodes from both linkedlist. The smaller node will get attached to the tail,
and becomes tail.
4. once the comparison is done, the node which got added to tail will change the ref to the next node.
5. If one linkedlist is all the way looped through, we append the other linkedlist node to the tail.
6. we return dummy_node.next since it is the actual head.
"""


from data_structures.Linked_List.Linked_List import Node


class Solution:
    def mergeTwoLists(self, list1_node: Node, list2_node: Node):
        dummy_node = Node()
        tail = dummy_node
        while list1_node and list2_node:
            if list1_node.value < list2_node.value:
                tail.next = list1_node
                list1_node = list1_node.next
            else:
                tail.next = list2_node
                list2_node = list2_node.next
            tail = tail.next
        if list1_node:
            tail.next = list1_node
        elif list2_node:
            tail.next = list2_node
        return dummy_node.next
