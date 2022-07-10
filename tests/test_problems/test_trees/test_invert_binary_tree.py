
"""
Test Suite for the 
"""
from problems.trees.invert_binary_tree import Solution
from data_structures.Trees.Binary_Search_Tree import BinarySearchTree, Node



class TestInvertTree:
    """
    Test Class
    """
    def test_one(self):
        bst = BinarySearchTree(4)
        bst.insert_node(2)
        bst.insert_node(7)
        bst.insert_node(1)
        bst.insert_node(3)
        bst.insert_node(6)
        bst.insert_node(9)
        inverted_bst_head = Solution().invertTree(bst.root)
        actual = BinarySearchTree.bfs_from_node(inverted_bst_head)
        expected = [4, 7, 2, 9, 6, 3, 1]
        assert actual == expected
        
    def test_two(self):
        bst = BinarySearchTree(2)
        bst.insert_node(1)
        bst.insert_node(3)
        inverted_bst_head = Solution().invertTree(bst.root)
        actual = BinarySearchTree.bfs_from_node(inverted_bst_head)
        expected = [2, 3, 1]
        assert actual == expected
