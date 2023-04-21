"""
Stack impementation using Linked List
LIFO
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return f"Node('{self.value}') --points-to-->{self.next}"
    


class Stack:
    def __init__(self, value=None) -> None:
        if value:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0
    def __str__(self) -> str:
        output = ""
        #output += "*"*5
        node = self.top
        while node is None:
            return "Empty Stack"
        while node is not None:
            output += f"\nNode: {node}\n"
            node = node.next
        #output += "\n"+"*"*5
        return output
    
    def __len__(self):
        return self.height
    
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
            
    def pop(self):
        if self.height == 0:
            print("Empty linked list. Cannout Pop")
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp        
        
        
        

            
"""
stack = Stack()
print(stack)
stack.push("Anton")
stack.push("Bob")
stack.push("Chris")
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
"""