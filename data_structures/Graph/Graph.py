"""
Graph Implementation
"""

class Graph:
    def __init__(self, value=None) -> None:
        self.adj_set = {}
        if value:
            self.adj_set.update({value: set()})
    
    def add_vertex(self, vx_value):
        if vx_value not in self.adj_set:
            self.adj_set.update({vx_value: set()})
            return True
        return False
    
    def remove_vertex(self, vx_value):
        if vx_value in self.adj_set:
            for edges in self.adj_set[vx_value]:
                self.adj_set[edges].discard(vx_value)
            del self.adj_set[vx_value]
            return True
        return False
        
    def add_edge(self, v1, v2):
        if v1 in self.adj_set and v2 in self.adj_set:
            self.adj_set[v1].add(v2)
            self.adj_set[v2].add(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_set and v2 in self.adj_set:
            self.adj_set[v1].discard(v2)
            self.adj_set[v2].discard(v1)
            return True
        return False
    
    def __str__(self):
        output = "----\n"
        for key, values in self.adj_set.items():
            edges = (", ").join(values)+"." if values else "None"
            output += f"{key}: {edges}\n"
        return output + "\n----\n"
    
    def __len__(self):
        return len(self.adj_set)
    

gp = Graph()
print(len(gp))
print(gp.add_vertex("A"))
print(gp.add_vertex("B"))
print(gp.add_vertex("C"))
print(gp.add_vertex("D"))
print(gp.add_edge("A","B"))
print(gp.add_edge("B","A"))
print(gp.add_edge("B","C"))
print(len(gp))
print((gp))
print(gp.remove_edge("A", "D"))
print(gp.remove_vertex("B"))
print(len(gp))
print((gp))