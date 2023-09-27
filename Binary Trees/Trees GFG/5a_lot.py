# Level Order Traversal
import queue

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
def levelOrderBottom(root):
    if root is None:
        return []
    
    qu = queue.Queue()
    qu.put(root)
    ans = []

    while not qu.empty():
        res = []
        size = qu.qsize()

        for _ in range(size):
            curr = qu.get()
            res.append(curr.val)
        
            if curr.left:
                qu.put(curr.left)
            
            if curr.right:
                qu.put(curr.right)
            
        ans.append(res)
    
    # return ans[::1] Normal LOT
    return ans[::-1]  # Reverse the order of the levels in the ans list





# Average of Levels in Binary Tree
def levelOrderTraversal(root):
    if root is None:
        return None
    
    res = []
    qu = queue.Queue()
    qu.put(root)

    while not qu.empty():
        size = qu.qsize()
        avg = 0.0

        for _ in range(size):
            curr = qu.get()
            avg += curr.data # only change

            if curr.left:
                qu.put(curr.left)
            
            if curr.right:
                qu.put(curr.right)
        
        res.append(avg / float(size))

    return res



# Bottom Left Tree Value
def findBottomLeftValue(root):
    if root is None:
        return 0
    qu = queue.Queue()
    qu.put(root)

    while not qu.empty():
        curr = qu.get()

        if curr.left:
            qu.put(curr.left)
        
        if curr.right:
            qu.put(curr.right)
    
    return curr.data