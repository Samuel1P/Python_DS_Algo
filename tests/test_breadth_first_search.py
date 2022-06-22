"""
Test Suite for the 
"""
import pytest
import random
from data_structures.Trees.Binary_Search_Tree import BinarySearchTree


class TestBFS:
    """
    Test Class
    """

    def test_bfs(self):
        bst1 = BinarySearchTree(5)
        bst1.insert_node(2)
        bst1.insert_node(8)
        bst1.insert_node(7)
        bst1.insert_node(9)
        bst1.insert_node(1)
        bst1.insert_node(3)
        actual = bst1.bfs()
        expected = [5, 2, 8, 1, 3, 7, 9]
        assert actual == expected
