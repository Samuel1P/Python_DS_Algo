"""
Linked List implimentation
"""
from __future__ import annotations
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
        return f"Node('{self.value}') --points-to--> {self.next}"
        
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
    
    def prepend(self, new_value):
        print("prepend called...")
        new_node = Node(new_value)
        if not self.length:
            print("Empty linked list.")
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    
    def prepend(self, new_value):
        print("prepend called...")
        new_node = Node(new_value)
        if not self.length:
            print("Empty linked list.")
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
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
    
    def pop_first(self):
        print("pop_first called..")
        if not self.length:
            print("Empty linked list. Cannout Pop_First")
            return None
        temp_head = self.head
        self.head = self.head.next
        temp_head.next = None
        self.length -= 1
        if not self.length:
            self.head = None
            self.tail = None
        return temp_head
    
    def get_node(self, index):
        print(f"get index {index}")
        if not self.length:
            print("Linked list is EMPTY")
            return None
        if index < 0 or index > self.length-1:
            print(f"Index {index} unavailable. Available index range till {len(self)-1}.")
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_node(self, index, value):
        print(f"set value {value} at index {index}...")
        temp = self.get_node(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert_node(self, index, value):
        new_node = Node(value)
        print(f"insert {new_node} at index {index}...")
        if index < 0 or index > self.length:
            print(f"Index {index} unavailable. Available index range till {len(self)}.")
            return False
        if index == 0:
            return self.prepend(new_node.value)
        if index == len(self):
            return self.append(new_node.value)
        temp_node = self.get_node(index-1)
        new_node.next = temp_node.next 
        temp_node.next = new_node
        self.length += 1
        return True     
    
    def remove_node(self, index):
        print(f"remove node at index {index}...")
        if index < 0 or index >= self.length:
            print(f"Index {index} unavailable. Available index range till {len(self)-1}.")
            return None
        if index == 0:
            return self.pop_first()
        if index == len(self)-1:
            return self.pop()
        temp_prev_node = self.get_node(index-1)
        temp_node = temp_prev_node.next
        temp_prev_node.next = temp_node.next 
        temp_node.next = None
        self.length -= 1
        return temp_node
    
    def reverse(self):
        after = self.head.next
        self.head, self.tail = self.tail, self.head
        temp = self.tail
        before = None
        for _ in range(len(self)):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    def print_all(self):
        print(f"Print all called : {len(self)}")
        temp_node = self.head
        while temp_node: 
            print(f"Node : {temp_node.value}")
            temp_node = temp_node.next
    
    def __len__(self):
        return self.length
    
LL1 = LinkedList("Ash")
# LL1 = LinkedList()
LL2 = LinkedList()

# LL2.print_all()

# LL1.prepend("Bob")
LL1.append("Bob")
LL1.append("Charlie")
# LL1.remove_node(2)
LL1.print_all()
LL1.reverse()
# LL1.print_all()
# LL1.remove_node(0)
LL1.print_all()
LL1.reverse()
# LL1.print_all()
# LL1.remove_node(0)
LL1.print_all()
# exit()
# LL1.print_all()

# LL1.prepend("Danny")
# LL1.prepend("Danny")
# LL1.print_all()
# LL2.append("Casper")
# LL2.print_all()
# print(LL1.pop())
# print(LL1.pop_first())
# print(LL1.get_node(0))
# print(LL1.set_node(0, 'Aaron'))
# print(LL1.set_node(1, 'Barry'))
# print(LL1.set_node(3, 'Cathy'))
# print(LL1.get_node(1))
# print(LL1.get_node(2))
# print(LL1.get_node(3))
# print(LL2.get_node(0))
# print(LL1.insert_node(4, 'Barry'))



# LL1.print_all()
