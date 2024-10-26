
"""
Test Suite for the reverse-linked-list-elements/
"""

from problems.linkedlist.reverse_linked_list import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestReverseElementsLinkedList:
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
        # self.LL2 = LinkedList(1)
        # self.LL2.append(1)
        # self.LL2.append(2)
        # self.LL2.append(3)
        # self.LL2.append(3)

    def test_one(self):
        expected = self.LL.traversed_data_list()
        expected.reverse()
        result_first_node = Solution().reverseList(self.LL.head)
        actual = self.LL.traversed_data_list_from_head(result_first_node)
        assert actual == expected

    def _test_two(self):
        element_to_remove = 1
        ll_head_updated = Solution().removeElements(self.LL_EMPTY.head, element_to_remove)
        actual = self.LL_EMPTY.traversed_data_list_from_head(ll_head_updated)
        expected = []
        assert actual == expected