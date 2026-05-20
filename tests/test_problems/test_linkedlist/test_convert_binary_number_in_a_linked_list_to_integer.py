"""
Test Suite for convert-binary-number-in-a-linked-list-to-integer
"""
from problems.linkedlist.convert_binary_number_in_a_linked_list_to_integer import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestConvertBinaryNumberInALinkedListToInteger:
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

    def test_one_leetcode_example_basic(self):
        """[1, 0, 1] is binary 101 -> 5."""
        ll = self._build_list([1, 0, 1])
        expected = 5
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_two_single_zero(self):
        """[0] -> 0. Edge case: single node with zero."""
        ll = self._build_list([0])
        expected = 0
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_three_single_one(self):
        """[1] -> 1. Edge case: single node with one."""
        ll = self._build_list([1])
        expected = 1
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_four_leetcode_example_long(self):
        """Long binary number from the LeetCode examples -> 18880."""
        ll = self._build_list([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        expected = 18880
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_five_all_ones(self):
        """[1, 1, 1] is binary 111 -> 7."""
        ll = self._build_list([1, 1, 1])
        expected = 7
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_six_all_zeros(self):
        """[0, 0, 0] -> 0. Leading zeros must not change the result."""
        ll = self._build_list([0, 0, 0])
        expected = 0
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_seven_power_of_two(self):
        """[1, 0, 0, 0] is binary 1000 -> 8."""
        ll = self._build_list([1, 0, 0, 0])
        expected = 8
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_eight_leading_zero(self):
        """[0, 1, 1] is binary 011 -> 3. Leading zero should not affect result."""
        ll = self._build_list([0, 1, 1])
        expected = 3
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_nine_mixed_bits(self):
        """[1, 1, 0, 1] is binary 1101 -> 13."""
        ll = self._build_list([1, 1, 0, 1])
        expected = 13
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected

    def test_ten_max_thirty_bits(self):
        """Thirty 1's -> 2^30 - 1 = 1073741823 (LeetCode upper bound)."""
        ll = self._build_list([1] * 30)
        expected = (1 << 30) - 1
        actual = Solution().getDecimalValue(ll.head)
        assert actual == expected
