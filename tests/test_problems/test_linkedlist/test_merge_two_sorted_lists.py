
"""
Test Suite for the merge sorted linked linked
"""
import pytest
import random
from problems.linkedlist.merge_two_sorted_lists import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestMergeSortedLinkedList:
    """
    Test Class
    """

    def setup_class(self):
        self.LL1 = LinkedList(1)
        self.LL1.append(2)
        self.LL1.append(3)
        self.LL1.append(3)
        self.LL1.append(3)
        self.LL1.append(5)
        self.LL2 = LinkedList(0)
        self.LL2.append(1)
        self.LL2.append(4)
        self.LL2.append(4)
        self.LL2.append(5)
        self.LL2.append(6)

        
    def test_one(self):
        merged_list_head  = Solution().mergeTwoLists(self.LL1.head, self.LL2.head)
        traversed_data_list_from_head = LinkedList().traversed_data_list_from_head(merged_list_head)
        expected = [0, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6]        
        assert traversed_data_list_from_head == expected
