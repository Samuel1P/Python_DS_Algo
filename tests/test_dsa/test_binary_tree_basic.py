"""
Test Suite for the Basic Binary tree
"""
from data_structures.Trees.Binary_Tree_Basic import TreeNode


class TestBinaryTree:
    """
    Test Class
    """

    def test_display_one(self):
        tree = TreeNode(5)
        tree.left = TreeNode(78)
        tree.right = TreeNode(2)
        tree.left.left = TreeNode(79)
        tree.left.right = TreeNode(80)
        actual = tree.in_order()
        expected = [79, 78, 80, 5, 2]
        assert actual == expected
    
    def test_display_two(self):
        tree = TreeNode(5)
        tree.left = TreeNode(78)
        tree.right = TreeNode(2)
        actual = tree.in_order()
        expected = [78, 5, 2]
        assert actual == expected