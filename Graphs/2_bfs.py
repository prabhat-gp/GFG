# BFS of Graph
import queue

def bfs(v, adj):
    ans = []
    visited = [0] * v
    qu = queue.Queue()
    qu.put(0)
    visited[0] = 1

    while not qu.empty():
        front = qu.get()
        ans.append(front)
        for i in adj[front]:
            if not visited[i]:
                qu.put(i)
                visited[i] = 1
    
    return ans







# Applications of BFS of A graph  :

# In peer-to-peer network like bit-torrent, BFS is used to find all neighbor nodes
# Search engine crawlers are used BFS to build index. Starting from source page, it finds all links in it to get new pages
# Using GPS navigation system BFS is used to find neighboring places.
# In networking, when we want to broadcast some packets, we use the BFS algorithm.
# Path finding algorithm is based on BFS .
# BFS is used in Ford-Fulkerson algorithm to find maximum flow in a network.
