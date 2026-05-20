"""
Test Suite for the remove-duplicates-from-unsorted-list

Two test classes — one per solution — running the same set of cases against
both the set-based approach (Solution1) and the runner-pointer approach
(Solution2). Both solutions mutate the linked list in place, so we check
the state of ll.head after each call (return value is ignored).
"""
from problems.linkedlist.remove_duplicates_from_unsorted_list import Solution1, Solution2
from data_structures.Linked_List.Linked_List import LinkedList


def _make_list(values):
    """Helper to build a LinkedList from a python list of values."""
    if not values:
        return LinkedList()
    ll = LinkedList(values[0])
    for value in values[1:]:
        ll.append(value)
    return ll


class TestRemoveDuplicatesFromUnsortedList:
    """
    Test Class for Solution1 (set-based, O(n) time / O(n) space).
    """

    def test_empty_list(self):
        ll = _make_list([])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = []
        assert actual == expected

    def test_single_node(self):
        ll = _make_list([42])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [42]
        assert actual == expected

    def test_no_duplicates(self):
        ll = _make_list([1, 2, 3, 4])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3, 4]
        assert actual == expected

    def test_unsorted_duplicates(self):
        ll = _make_list([12, 11, 12, 21, 41, 43, 21])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [12, 11, 21, 41, 43]
        assert actual == expected

    def test_multiple_repetitions(self):
        ll = _make_list([1, 2, 1, 3, 2, 4, 1, 5, 3])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3, 4, 5]
        assert actual == expected

    def test_all_duplicates(self):
        ll = _make_list([9, 9, 9, 9])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [9]
        assert actual == expected

    def test_duplicates_at_beginning(self):
        ll = _make_list([5, 5, 1, 2, 3])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [5, 1, 2, 3]
        assert actual == expected

    def test_duplicates_at_end(self):
        ll = _make_list([1, 2, 3, 7, 7])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3, 7]
        assert actual == expected

    def test_consecutive_duplicates(self):
        ll = _make_list([1, 1, 2, 2, 3, 3])
        Solution1().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3]
        assert actual == expected


class TestRemoveDuplicatesFromUnsortedListRunner:
    """
    Test Class for Solution2 (runner pointer, O(n^2) time / O(1) space).
    """

    def test_empty_list(self):
        ll = _make_list([])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = []
        assert actual == expected

    def test_single_node(self):
        ll = _make_list([42])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [42]
        assert actual == expected

    def test_no_duplicates(self):
        ll = _make_list([1, 2, 3, 4])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3, 4]
        assert actual == expected

    def test_unsorted_duplicates(self):
        ll = _make_list([12, 11, 12, 21, 41, 43, 21])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [12, 11, 21, 41, 43]
        assert actual == expected

    def test_multiple_repetitions(self):
        ll = _make_list([1, 2, 1, 3, 2, 4, 1, 5, 3])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3, 4, 5]
        assert actual == expected

    def test_all_duplicates(self):
        ll = _make_list([9, 9, 9, 9])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [9]
        assert actual == expected

    def test_duplicates_at_beginning(self):
        ll = _make_list([5, 5, 1, 2, 3])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [5, 1, 2, 3]
        assert actual == expected

    def test_duplicates_at_end(self):
        ll = _make_list([1, 2, 3, 7, 7])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3, 7]
        assert actual == expected

    def test_consecutive_duplicates(self):
        ll = _make_list([1, 1, 2, 2, 3, 3])
        Solution2().removeDuplicates(ll.head)
        actual = LinkedList.traversed_data_list_from_head(ll.head)
        expected = [1, 2, 3]
        assert actual == expected
