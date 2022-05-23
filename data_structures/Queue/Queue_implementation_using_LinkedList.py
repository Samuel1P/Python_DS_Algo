"""
Queue impementation using Linked List
FIFO
"""
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return f"Node('{self.value}') --points-to-->{self.next}"
    


class Queue:
    def __init__(self, value=None) -> None:
        if value:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.height = 1
        else:
            self.first = None
            self.last = None
            self.height = 0

    def __str__(self) -> str:
        output = ""
        output += "*"*50
        node = self.first
        while node is not None:
            output += f"\nNode: {node}\n"
            node = node.next
        output += "\n"+"*"*50
        return output
    
    def enqeue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.height += 1
        
    def deqeue(self):
        if self.height == 0:
            print("Empty linked list. Cannout Pop_First")
            return None
        temp = self.first
        if self.height == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.height -= 1
        return temp

q = Queue()
q.enqeue("Anto")
q.enqeue("Brad")

print(q)
q.deqeue()
q.deqeue()
print(q)