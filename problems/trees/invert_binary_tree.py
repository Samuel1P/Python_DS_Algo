"""
invert_binary_tree
https://leetcode.com/problems/invert-binary-tree/

Notes:
1. We will do a depth first search (Recursion).
2. Exit or Base condition will be when node is None, we return None which removed one item from the call stack.
3. Swap the left and right nodes.
4. Recurse the same method to the swapped nodes.
5. The root node remains the same. Return it at the end.
"""

from data_structures.Trees.Binary_Search_Tree import BinarySearchTree, Node

class Solution:
    def invertTree(self, curr_node: Node) -> Node:
        if not curr_node:
            return None
        curr_node.left, curr_node.right = curr_node.right, curr_node.left
        Solution().invertTree(curr_node.left)
        Solution().invertTree(curr_node.right)
        return curr_node