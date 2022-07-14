
"""
Test Suite for the remove-linked-list-elements/
"""

from problems.linkedlist.remove_linked_list_elements import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestRemoveElementsLinkedList:
    """
    Test Class
    """

    def setup_class(self):
        self.LL_EMPTY = LinkedList(1)
        self.LL = LinkedList(1)
        self.LL.append(1)
        self.LL.append(2)
        self.LL.append(3)
        self.LL.append(3)
        self.LL.append(4)
        self.LL.append(3)
        self.LL.append(5)
        self.LL.append(3)
        
    def test_one(self):
        element_to_remove = 3
        ll_head_updated = Solution().removeElements(self.LL.head, element_to_remove)
        actual = self.LL.traversed_data_list_from_head(ll_head_updated)
        expected = [1, 1, 2, 4, 5]
        assert actual == expected

    def test_two(self):
        element_to_remove = 1
        ll_head_updated = Solution().removeElements(self.LL_EMPTY.head, element_to_remove)
        actual = self.LL_EMPTY.traversed_data_list_from_head(ll_head_updated)
        expected = []
        assert actual == expected