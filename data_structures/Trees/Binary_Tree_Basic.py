"""
Basic Binary Tree implementation
"""
from __future__ import annotations
from functools import total_ordering

@total_ordering
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"Node('{self.val}')"
    
    def __eq__(self, other_node):
        if not isinstance(other_node, TreeNode):
            return NotImplemented
        return self.val == other_node.val
    
    def __gt__(self, other_node):
        if not isinstance(other_node, TreeNode):
            return NotImplemented
        return self.val > other_node.val
    
    def in_order(self):
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)
        traverse(self)
        return result