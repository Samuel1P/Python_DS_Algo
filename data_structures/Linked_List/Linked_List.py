"""
Linked List implimentation
"""
from __future__ import annotations
from tkinter.messagebox import NO

class Node:
    """
    Node Class
    """
    def __init__(self, value):
        """
        Constructor for Node
        """
        self.value = value
        self.next = None
    
    def __repr__(self):
        """
        str represention of the node
        """
        return f"Node('{self.value}') --points-to--> Node('{self.next}'))"
        
class LinkedList:
    """
    Linked List Class
    """
    def __init__(self, value=None):
        """
        constructor for linked list
        """
        if value:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
    
    def append(self, new_value):
        print("append called..")
        node = Node(new_value)
        if not self.length:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
    
    def pop(self):
        print("pop called..")
        if not self.length:
            print("Empty linked list. Cannout Pop")
            return None
        temp_node = self.head
        pre = self.head
        while temp_node.next:
            pre = temp_node
            temp_node = temp_node.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if not self.length:
            self.head = None
            self.tail = None
        return temp_node
    
    def prepend(self, new_value):
        print("prepend called...")
        new_node = Node(new_value)
        if not self.length:
            print("Empty linked list.")
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        
    def print_all(self):
        print("Print all called :")
        temp_node = self.head
        while temp_node:
            print(f"Node : {temp_node.value}")
            temp_node = temp_node.next
    
    def __len__(self):
        return self.length
    
LL1 = LinkedList("Abi")
#LL2 = LinkedList()

LL1.print_all()
# LL2.print_all()

LL1.prepend("Bob")
LL1.append("Charlie")
# LL1.append("Charlie")
LL1.prepend("Danny")
# LL1.prepend("Danny")
LL1.print_all()
# LL2.append("Casper")
# LL2.print_all()
LL1.pop()
LL1.print_all()
