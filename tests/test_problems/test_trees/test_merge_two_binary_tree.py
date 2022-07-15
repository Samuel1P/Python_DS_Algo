
"""
Test Suite for the 
"""
from problems.trees.merge_two_binary_trees import Solution
from data_structures.Trees.Binary_Tree_Basic import TreeNode



class TestMergeBinaryTree:
    """
    Test Class
    """
    def test_one(self):
        a1 = TreeNode(1)
        a3 = TreeNode(3)
        a5 = TreeNode(5)
        a7 = TreeNode(7)
        a9 = TreeNode(9)
        a11 = TreeNode(11)
        b2 = TreeNode(2)
        b4 = TreeNode(4)
        b6 = TreeNode(6)
        b8 = TreeNode(8)
        b10 = TreeNode(10)

        a1.left = a3
        a1.right = a5
        a3.left = a7
        a3.right = a9
        a5.left = a11
        
        b2.left = b4
        b2.right = b6
        b4.left = b8
        b6.right = b10
        merged_tree = Solution().mergeTrees(a1, b2)
        actual = merged_tree.in_order()
        expected = [15, 7, 9, 3, 11, 11, 10]
        assert actual == expected

