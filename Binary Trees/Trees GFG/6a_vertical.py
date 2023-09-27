# Vertical Order Traversal of Binary Tree
import queue

def verticalOrder(root):
    if root is None:
        return [0]
    
    map = {}
    qu = queue.Queue()
    qu.put((root, 0))

    while not qu.empty():
        curr, temp = qu.get()
        if temp in map:
            map[temp].append(curr.data)
        else:
            map[temp] = [curr.data] # important

        if curr.left:
            qu.put((curr.left, temp - 1))
        
        if curr.right:
            qu.put((curr.right, temp + 1))

    ans = []
    for i in sorted(map.keys()):
        for ele in map[i]:
            ans.append(ele)
        
    return ans



# Leetcode Approach (Forget it)
from collections import defaultdict
def verticalOrder(root):
    if root is None:
        return []
    
    map = defaultdict(list)
    qu = queue.Queue()
    qu.put((root, 0, 0))
    ans = []

    while not qu.empty():
        curr, temp, vt = qu.get()
        map[temp].append((vt, curr.data))

        if curr.left:
            qu.put((curr.left, temp - 1, vt + 1))
        
        if curr.right:
            qu.put((curr.right, temp + 1, vt + 1))

    for i in sorted(map.keys()):
        nodes = [val for vertical_dist, val in sorted(map[i])]
        ans.append(nodes)
        
    return ans