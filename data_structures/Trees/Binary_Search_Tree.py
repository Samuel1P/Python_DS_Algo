"""
Binary Search Tree implementation
"""

from functools import total_ordering

@total_ordering
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"Node('{self.value}')"
    
    def __eq__(self, other_node):
        if not isinstance(other_node, Node):
            return NotImplemented
        return self.value == other_node.value
    
    def __gt__(self, other_node):
        if not isinstance(other_node, Node):
            return NotImplemented
        return self.value > other_node.value
        
class BinarySearchTree:
    def __init__(self, value=None):
        if value:
            new_node = Node(value)
            self.root = new_node
            print("root added")
        else:
            self.root = None
        
    def insert_node(self, new_value):
        new_node = Node(new_value)
        if self.root == None:
            self.root = new_node
            print("root added")
            return True
        temp = self.root
        while True:
            if new_node == temp:
                print(f"Node with same value exists: {new_node}")
                return False
            elif new_node < temp:
                if not temp.left:
                    temp.left = new_node
                    print("added node to a left")
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    print("added node to a right")
                    return True
                temp = temp.right
    
    def contains_value(self, value):
        target = Node(value)
        if self.root is None:
            print("Empty BST.")
            return False
        temp = self.root
        while temp:
            if target < temp:
                temp = temp.left 
            elif target > temp:
                temp = temp.right
            else:
                assert target == temp
                print("Found target")
                return True
        print("Value NOT FOUND")
        return False
    
    def get_node(self, value):
        if not self.contains_value(value):
            return None
        target = Node(value)
        temp = self.root
        while temp:
            if target < temp:
                temp = temp.left 
            elif target > temp:
                temp = temp.right
            else:
                assert target == temp
                print("Found target")
                return temp
        print("Value NOT FOUND")
        return None


    def minimum_value(self, value=None):
        if value is None:
            value = self.root.value
        if not self.contains_value(value):
            return False
        curr_node = self.get_node(value)
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node
    
    def maximum_value(self, value=None):
        if value is None:
            value = self.root.value
        if not self.contains_value(value):
            return False
        curr_node = self.get_node(value)
        while curr_node.right is not None:
            curr_node = curr_node.right
        return curr_node

    """
    # TO DO
    def delete_node(self, value):
        # Delete a node and all its children (if any from the BST)
    
    def __str__(self):
        # Write a method to provide a string represention of Trees.
        # Similar to what we have in "binary_tree.txt"
        # Need to learn Tree traversal to implement this
    """
    
    
bst1 = BinarySearchTree(5)
print(bst1.root)
bst1.insert_node(2)
bst1.insert_node(8)
bst1.insert_node(7)
bst1.insert_node(9)
print(bst1.root.left, bst1.root, bst1.root.right)
bst1.contains_value(0)
print(bst1.get_node(2))
print("- Min Value-")
print(bst1.minimum_value(8))
print("- Max Value-")
print(bst1.maximum_value(8))