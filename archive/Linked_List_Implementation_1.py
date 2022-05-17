# Linked list implementation of insert head and insert tail

class Node():
    def __init__(self, data):
        self.data = data
        self.NextNode = None

    def __repr__(self):
        return f"node('data --> {self.data}', reference ----> {self.NextNode})"

class Linked_List():
    def __init__(self):
        self.length = 0
        self.head = None

    def insert_start(self, node_):
        self.length = self.length + 1
        self.head = node_

    def insert_end(self, node_):
        self.length = self.length + 1
        self.current_node = self.head
        while self.current_node.NextNode is not None: # see if if this is the last node or if there is a ref to another node - exit when it finds the last node
            self.current_node = self.current_node.NextNode # if there is another node, go to that node
        self.current_node.NextNode = node_ # once the last node is found, set the reference for this node to the new node.

    def print_list(self):
        self.current_node = self.head
        for i in range(self.length):
            print (f"NODE #{i+1}--- > {self.current_node.__repr__()}")
            self.current_node = self.current_node.NextNode



node1 = Node("Anish")
obj = Linked_List()
obj.insert_start(node1)
obj.print_list() # NODE #1--- > node('data --> Anish', reference ----> None)
node2 = Node("Carlsen")
node3 = Node("Naka")
obj.insert_end(node2)
obj.insert_end(node3)
obj.print_list()
"""
Output:
NODE #1--- > node('data --> Anish', reference ----> node('data --> Carlsen', reference ----> node('data --> Naka', reference ----> None)))
NODE #2--- > node('data --> Carlsen', reference ----> node('data --> Naka', reference ----> None))
NODE #3--- > node('data --> Naka', reference ----> None)
"""


