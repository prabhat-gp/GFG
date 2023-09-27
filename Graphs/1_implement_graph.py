# Implement Graph

class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, u, v, direction):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
        if direction == 0:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)
    
    def printAdjList(self):
        for vertex, neighbors in self.graph.items():
            print(vertex, "->", neighbors)

g = Graph()

g.addEdge(0, 1, 1)
g.addEdge(1, 2, 1)
g.addEdge(2, 3, 1)
g.addEdge(3, 0, 1)

print("Adjacency List:")
g.printAdjList()

'''
0 -> 1
↑    ↓
3 <- 2
'''
