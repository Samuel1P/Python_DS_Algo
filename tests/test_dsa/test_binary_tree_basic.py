"""
Test Suite for the Basic Binary tree
"""
from data_structures.Trees.Binary_Tree_Basic import BinaryTreeNode


class TestBinaryTree:
    """
    Test Class
    """

    def test_display_one(self):
        tree = BinaryTreeNode(5)
        tree.left = BinaryTreeNode(78)
        tree.right = BinaryTreeNode(2)
        tree.left.left = BinaryTreeNode(79)
        tree.left.right = BinaryTreeNode(80)
        actual = tree.in_order()
        expected = [79, 78, 80, 5, 2]
        assert actual == expected
    
    def test_display_two(self):
        tree = BinaryTreeNode(5)
        tree.left = BinaryTreeNode(78)
        tree.right = BinaryTreeNode(2)
        actual = tree.in_order()
        expected = [78, 5, 2]
        assert actual == expected