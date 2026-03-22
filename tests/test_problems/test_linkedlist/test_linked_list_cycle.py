"""
Test Suite for linked-list-cycle
"""
from problems.linkedlist.linked_list_cycle import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestLinkedListCycle:
    """
    Test Class
    """

    def _build_list(self, values):
        if not values:
            return LinkedList()

        linked_list = LinkedList(values[0])
        for value in values[1:]:
            linked_list.append(value)
        return linked_list

    def test_one_no_cycle(self):
        """
        Linear list with no loop should return False.
        """
        ll = self._build_list([1, 2, 3, 4, 5])
        assert Solution().has_loop(ll.head) is False

    def test_two_tortoise_hare_detects_cycle(self):
        """
        Loop from tail to a middle node should return True.
        """
        ll = self._build_list([10, 20, 30, 40, 50])
        ll.tail.next = ll.get_node(2)
        assert Solution().has_loop(ll.head) is True

    def test_three_single_node_no_cycle(self):
        """
        Single node with no back-edge should return False.
        """
        ll = self._build_list([7])
        assert Solution().has_loop(ll.head) is False

    def test_four_single_node_self_loop(self):
        """
        Single node pointing to itself should return True.
        """
        ll = self._build_list([7])
        ll.head.next = ll.head
        assert Solution().has_loop(ll.head) is True

    def test_five_empty_list_no_cycle(self):
        """
        Empty list should return False.
        """
        ll = self._build_list([])
        assert Solution().has_loop(ll.head) is False

    def test_six_none_input_no_cycle(self):
        """
        Passing None as head should return False.
        """
        assert Solution().has_loop(None) is False

    def test_seven_two_node_no_cycle(self):
        """
        Two node linear list should return False.
        """
        ll = self._build_list([1, 2])
        assert Solution().has_loop(ll.head) is False

    def test_eight_two_node_cycle(self):
        """
        Two node list with tail pointing back to head should return True.
        """
        ll = self._build_list([1, 2])
        ll.tail.next = ll.head
        assert Solution().has_loop(ll.head) is True

    def test_nine_cycle_at_head(self):
        """
        Multi-node cycle to head should return True.
        """
        ll = self._build_list([5, 6, 7, 8])
        ll.tail.next = ll.head
        assert Solution().has_loop(ll.head) is True

    def test_ten_compatibility_with_hasCycle_name(self):
        """
        LeetCode wrapper method should behave same as has_loop.
        """
        ll = self._build_list([1, 2, 3, 4])
        ll.tail.next = ll.get_node(1)
        assert Solution().hasCycle(ll.head) is True
