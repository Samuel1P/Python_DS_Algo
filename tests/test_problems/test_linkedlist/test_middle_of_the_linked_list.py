"""
Test Suite for the middle of the linked list
"""
from problems.linkedlist.middle_of_the_linked_list import Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestMiddleOfTheLinkedList:
    """
    Test Class
    """
    def setup_class(self):
        self.LL_ODD = LinkedList(1)
        self.LL_ODD.append(2)
        self.LL_ODD.append(3)
        self.LL_ODD.append(4)
        self.LL_ODD.append(5)

        self.LL_EVEN = LinkedList(1)
        self.LL_EVEN.append(2)
        self.LL_EVEN.append(3)
        self.LL_EVEN.append(4)
        self.LL_EVEN.append(5)
        self.LL_EVEN.append(6)

        self.LL_SINGLE = LinkedList(10)

        self.LL_TWO = LinkedList(1)
        self.LL_TWO.append(2)

        self.LL_EMPTY = LinkedList()

    def test_one(self):
        """
        Odd length list: 1 -> 2 -> 3 -> 4 -> 5
        Middle should be 3.
        """
        actual_middle_node = Solution().find_middle_node(self.LL_ODD.head)
        expected = 3
        assert actual_middle_node.val == expected

    def test_two(self):
        """
        Even length list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        Middle should be the second one of the two middle nodes => 4.
        """
        actual_middle_node = Solution().find_middle_node(self.LL_EVEN.head)
        expected = 4
        assert actual_middle_node.val == expected

    def test_three(self):
        """
        Single element list should return itself.
        """
        actual_middle_node = Solution().find_middle_node(self.LL_SINGLE.head)
        assert actual_middle_node.val == 10

    def test_four(self):
        """
        Two element list should return the second element.
        """
        actual_middle_node = Solution().find_middle_node(self.LL_TWO.head)
        assert actual_middle_node.val == 2

    def test_five(self):
        """
        Empty list should return None.
        """
        actual_middle_node = Solution().find_middle_node(self.LL_EMPTY.head)
        assert actual_middle_node is None

    def test_regression_fast_pointer_guard(self):
        """
        Regression for loop-guard bug:
        `while slow_ptr and fast_ptr.next` can crash when fast_ptr becomes None.
        """
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        ll.append(40)
        ll.append(50)

        actual_middle_node = Solution().find_middle_node(ll.head)
        assert actual_middle_node.val == 30
