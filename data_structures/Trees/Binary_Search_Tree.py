"""
Binary Search Tree implimentation
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"Node('{self.value}')"
    

class BinarySearchTree:
    def __init__(self, value=None):
        if value:
            new_node = Node(value)
            self.root = new_node
        else:
            self.root = None
        
        
    def __str__(self):
        # TO DO
        # Write a method to provide a string represention of Trees.
        # Similar to what we have in "binary_tree.txt"
        pass
    
    
bst1 = BinarySearchTree(5)
print(bst1.root)