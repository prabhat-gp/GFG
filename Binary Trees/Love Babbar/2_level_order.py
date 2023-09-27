import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# LOT
def levelOrderTraversal(root):
    if root is None:
        return []
    
    res = []
    qu = queue.Queue()
    qu.put(root)

    while not qu.empty():
        curr = qu.get()
        res.append(curr.data)

        if curr.left:
            qu.put(curr.left)
        
        if curr.right:
            qu.put(curr.right)

    return res



# Reverse LOT
def reverseLevelOrder(root):
    if root is None:
        return []
    
    qu = queue.Queue()
    qu.put(root)
    ans = []

    while not qu.empty():
        v = []
        size = qu.qsize()

        for i in range(size):
            curr = qu.get()
            v.append(curr.data)

            if curr.left:
                qu.put(curr.left)
            
            if curr.right:
                qu.put(curr.right)

        ans = v + ans
    
    return ans

        