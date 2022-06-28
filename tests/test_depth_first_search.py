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

    def setup_method(self):
        self.bst1 = BinarySearchTree(5)
        self.bst1.insert_node(2)
        self.bst1.insert_node(8)
        self.bst1.insert_node(7)
        self.bst1.insert_node(9)
        self.bst1.insert_node(1)
        self.bst1.insert_node(3)
        
    def test_dfs_preorder(self):

        actual = self.bst1.dfs_preorder()
        expected = [5, 2, 1, 3, 8, 7, 9]
        assert actual == expected
