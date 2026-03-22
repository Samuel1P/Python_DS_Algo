"""
Test Suite for find-kth-node-from-end
"""
from problems.linkedlist.find_kth_node_from_end import find_kth_from_end
from data_structures.Linked_List.Linked_List import LinkedList


class TestFindKthNodeFromEnd:
    """
    Test Class
    """

    def setup_class(self):
        self.LL = LinkedList(1)
        self.LL.append(2)
        self.LL.append(3)
        self.LL.append(4)
        self.LL.append(5)
        self.LL.append(6)
        self.LL.append(7)
        self.LL.append(8)
        self.LL.append(9)

        self.LL_SINGLE = LinkedList(10)

        self.LL_EMPTY = LinkedList()

    def test_empty_list(self):
        """
        Empty list: should return -1 for any k.
        Validates how the function behaves when the input list is [].
        """
        result = find_kth_from_end(self.LL_EMPTY, 1)
        assert result == -1

    def test_k_equal_to_length(self):
        """
        k equals list length: should return the head node value.
        For list [1->2->3->4->5->6->7->8->9], k=9 should return 1.
        Checks the logic when k is exactly the size of the list.
        """
        result = find_kth_from_end(self.LL, 9)
        assert result == 1

    def test_k_less_than_length(self):
        """
        k less than length: standard case within bounds.
        For list [1->2->3->4->5->6->7->8->9], k=2 should return 8.
        The "happy path" where k is a standard value within the list's bounds.
        """
        result = find_kth_from_end(self.LL, 2)
        assert result == 8

    def test_k_more_than_length(self):
        """
        k exceeds list length: should return -1.
        For list [1->2->3->4->5->6->7->8->9], k=10 should return -1.
        Ensures the function returns -1 when k exceeds the list size.
        """
        result = find_kth_from_end(self.LL, 10)
        assert result == -1
