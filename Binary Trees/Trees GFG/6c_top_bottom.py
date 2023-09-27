# Top View of Binary Tree
import queue

def topView(root):
    if root is None:
        return []
    
    map = {}
    qu = queue.Queue()
    qu.put((root, 0))

    while not qu.empty():
        curr, temp = qu.get()
        if temp not in map:
            map[temp] = curr.data # important
        
        if curr.left:
            qu.put((curr.left, temp - 1))

        if curr.right:
            qu.put((curr.right, temp + 1))

    ans = []
    for key in sorted(map):  
        ans.append(map[key])

    return ans



# Bottom View
# Approach 1
def bottomView(root):
    if root is None:
        return []
    
    map = {}
    qu = queue.Queue()
    qu.put((root, 0))

    while not qu.empty():
        curr, temp = qu.get()
        
        map[temp] = curr.data # important
        
        if curr.left:
            qu.put((curr.left, temp - 1))

        if curr.right:
            qu.put((curr.right, temp + 1))

    ans = []
    for key in sorted(map):  
        ans.append(map[key])

    return ans



# Approach 2
def bottomView(root):
    if root is None:
        return []
    
    map = {}
    qu = queue.Queue()
    qu.put((root, 0))

    minDis = float("inf")
    maxDis = float("-inf")

    while not qu.empty():
        curr, temp = qu.get()

        minDis = min(minDis, temp)
        maxDis = max(maxDis, temp)

        map[temp] = curr.data

        if curr.left:
            qu.put((curr.left, temp - 1))
        
        if curr.right:
            qu.put((curr.right, temp + 1))
    
    res = []
    for i in range(minDis, maxDis + 1):
        res.append(map[i])
    
    return res




