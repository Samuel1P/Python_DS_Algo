
"""
Test Suite for the rotate-list
"""

from problems.linkedlist.rotate_list import Solution as Solution
from data_structures.Linked_List.Linked_List import LinkedList


class TestRotateList:
    """
    Test Class
    """

    def setup_method(self):
        self.LL_EMPTY = LinkedList(1)
        self.LL = LinkedList(1)
        self.LL.append(2)
        self.LL.append(3)
        self.LL.append(4)
        self.LL.append(5)
        self.LL.append(6)
        self.LL.append(7)
        self.LL.append(8)
        
    def test_one(self):
        rotate_k_places = 3
        ll_head_updated = Solution().rotateRight(self.LL.head, rotate_k_places)
        actual = self.LL.traversed_data_list_from_head(ll_head_updated)
        expected = [6,7,8,1,2,3,4,5] # [1, 2, 3, 4, 4, 3, 5, 3]
        assert actual == expected

    def test_two(self):
        rotate_k_places = 1
        ll_head_updated = Solution().rotateRight(self.LL_EMPTY.head, rotate_k_places)
        actual = self.LL_EMPTY.traversed_data_list_from_head(ll_head_updated)
        expected = [1]
        assert actual == expected
        
    def test_three(self):
        rotate_k_places = 10
        ll_head_updated = Solution().rotateRight(self.LL.head, rotate_k_places)
        actual = self.LL.traversed_data_list_from_head(ll_head_updated)
        expected = [7,8,1,2,3,4,5,6]
        assert actual == expected
        
    def test_four(self):
        rotate_k_places = 8
        ll_head_updated = Solution().rotateRight(self.LL.head, rotate_k_places)
        actual = self.LL.traversed_data_list_from_head(ll_head_updated)
        expected = [1, 2, 3, 4, 5,6,7,8]
        assert actual == expected