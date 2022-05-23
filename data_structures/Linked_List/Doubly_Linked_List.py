"""
Doubly Linked List implementation
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
        self.prev = None
        self.next = None
      
    def __repr__(self):
        """
        str represention of the node
        """
        #return f"Node('{self.value}') --points-to--> {self.next}"
        return f"Node('{self.value}')"
    
class DoublyLinkedList:
    def __init__(self, value=None) -> None:
        if value:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
    
    def append(self, new_value: str) -> bool:
        new_node = Node(new_value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
        self.length += 1
        return True
    
    
    def prepend(self, new_value: str) -> bool:
        new_node = Node(new_value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    
    def pop(self) -> Node:
        if self.length == 0:
            print("Empty Double Linked List")
            return
        temp = self.tail  
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 0
        return temp
    
    def pop_first(self) -> Node:
        if self.length == 0:
            print("Empty Double Linked List")
            return
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 0
        return temp
    
    def get_node(self, index: int) -> Node:
        if index >= len(self) or index < 0:
            #print(f"GET ERROR: Out of bound index . Expected index till {len(self)-1}")
            return None
        if self.length == 0:
            print("GET ERROR: Empty Double Linked List")
            return None
        if index < len(self)/2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(len(self)-1, index, -1):
                node = node.prev
        return node

    def set_node(self, index: int, value: str) -> bool:
        node = self.get_node(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert_node(self, index: int, value: str) -> bool:
        if index > len(self) or index < 0:
            print(f"INSERT ERROR: Out of bound index. Expected index till {len(self)-1}")
            return False
        new_node = Node(value)
        if index == 0:
            return self.prepend(new_node.value)
        if index == len(self):
            return self.append(new_node.value)
        before = self.get_node(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node 
        self.length += 1
        return True
        
        
    def remove_node(self, index: int) -> Node:
        if index >= len(self) or index < 0:
            print(f"INSERT ERROR: Out of bound index. Expected index till {len(self)-1}")
            return False
        if index == 0:
            return self.pop_first()
        if index == len(self)-1:
            return self.pop(index)
        temp = self.get_node(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp
        
        
    def __len__(self):
        return self.length
    
    def __repr__(self):
        """
        str represention of the DLL
        """
        print("-"*50)
        print(f"Head Node: {self.head}")
        print(f"Tail Node: {self.tail}")
        output = ""
        node = self.head
        while node is not None:
            output += f"{str(node)} > "
            node = node.next
        return output+"\n"+"-"*50

DL = DoublyLinkedList("Abi")
DL.prepend("Bob")
DL.prepend("Cathy")
DL.append("Dan")
# print(DL)
# print(DL.get_node(3))
# print(DL.get_node(2))
# print(DL.get_node(1))
print(DL)

print(DL.remove_node(0))
print(DL.insert_node(0, "Aakash"))
print(DL)
# print(DL.pop())
DL = DoublyLinkedList()

print(DL)