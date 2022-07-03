
"""
Test Suite for the remove-duplicates-from-sorted-list/submissions/
"""
import pytest
import random
from problems.linkedlist.remove_duplicates_from_sorted_list import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestTwoSum:
    """
    Test Class
    """

    def setup_class(self):
        self.LL_EMPTY = LinkedList()
        self.LL = LinkedList(1)
        self.LL.append(1)
        self.LL.append(2)
        self.LL.append(3)
        self.LL.append(3)
        self.LL.append(3)
        self.LL.append(5)
        
    def test_one(self):
        traversed_data_list = self.LL.traversed_data_list()
        head_without_dups = Solution().deleteDuplicates(self.LL.head)
        traversed_data_list_from_head = self.LL.traversed_data_list_from_head(head_without_dups)
        assert list(set(traversed_data_list)) == traversed_data_list_from_head

    def test_two(self):
        traversed_data_list = self.LL_EMPTY.traversed_data_list()
        head_without_dups = Solution().deleteDuplicates(self.LL_EMPTY.head)
        traversed_data_list_from_head = self.LL_EMPTY.traversed_data_list_from_head(head_without_dups)
        assert list(set(traversed_data_list)) == traversed_data_list_from_head