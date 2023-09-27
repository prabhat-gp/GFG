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

# Create a graph
g = Graph()

# Take input for the number of nodes and edges
num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))

# Add edges based on input
for _ in range(num_edges):
    u, v, direction = map(int, input("Enter edge (u v direction): ").split())
    g.addEdge(u, v, direction)

# Print the adjacency list
print("Adjacency List:")
g.printAdjList()

'''

Enter the number of nodes: 4
Enter the number of edges: 4
Enter edge (u v direction): 0 1 1
Enter edge (u v direction): 1 2 1
Enter edge (u v direction): 2 3 1
Enter edge (u v direction): 3 0 1
Adjacency List:
0 -> [1]
1 -> [2]
2 -> [3]
3 -> [0]

'''