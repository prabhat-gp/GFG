# Given a binary tree find the minimum time required to burn the complete binary tree if the target is set on fire. (Hard)


import queue

def createParent(root, target, nodeToParent):
    res = None
    qu = queue.Queue()
    qu.put(root)
    nodeToParent[root] = None
    
    while not qu.empty():
        front = qu.get()
        
        if front.data == target:
            res = front
        
        if front.left:
            nodeToParent[front.left] = front
            qu.put(front.left)
        
        if front.right:
            nodeToParent[front.right] = front
            qu.put(front.right)
    
    return res

def burnTree(targetNode, nodeToParent):
    visited = {}
    qu = queue.Queue()
    qu.put(targetNode)
    visited[targetNode] = True
    ans = 0
    
    while not qu.empty():
        size = qu.qsize()
        flag = 0
        
        for i in range(size):
            front = qu.get()
            if front.left and not visited.get(front.left, False):
                flag = 1
                qu.put(front.left)
                visited[front.left] = True
            
            if front.right and not visited.get(front.right, False):
                flag = 1
                qu.put(front.right)
                visited[front.right] = True
                
            if nodeToParent[front] and not visited.get(nodeToParent[front], False):
                flag = 1
                qu.put(nodeToParent[front])
                visited[nodeToParent[front]] = True
        
        if flag == 1:
            ans += 1
    
    return ans

def minTime(root, target):
    ans = 0
    nodeToParent = {}
    targetNode = createParent(root, target, nodeToParent)
    
    ans = burnTree(targetNode, nodeToParent)
    return ans
