# Vertical Width of a Binary Tree
import queue

def verticalWidth(root):
    if root is None:
        return 0
    
    minDis = float("inf")
    maxDis = float("-inf")

    qu = queue.Queue()
    qu.put((root, 0))

    while not qu.empty():
        curr, temp = qu.get()

        minDis = min(minDis, temp)
        maxDis = max(maxDis, temp)

        if curr.left:
            qu.put((curr.left, temp - 1))

        if curr.right:
            qu.put((curr.right, temp + 1))
        
    
    total = maxDis - minDis + 1
    return total



# Maximum Width of Tree
# Width = No of nodes btw any 2 nodes

def maxWidth(root):
    if root is None:
        return 0
    
    qu = queue.Queue()
    qu.put((root, 0))
    max_width = 0

    while not qu.empty():
        size = qu.qsize()
        firstIndex = -1

        for i in range(size):
            curr, index = qu.get()

            if i == 0:
                firstIndex = index

            if curr.left:
                qu.put((curr.left, 2 * index))
            
            if curr.right:
                qu.put((curr.right, 2 * index + 1))
        
        max_width = max(max_width, index - firstIndex + 1)
    
    return max_width

        