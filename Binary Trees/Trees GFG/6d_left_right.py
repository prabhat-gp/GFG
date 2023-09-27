# Left View
# First Node in Every Level

def solve(root, ans, level):
    if root is None:
        return
    if level == len(ans):
        ans.append(root.data)
    solve(root.left, ans, level + 1)
    solve(root.right, ans, level + 1)



def LeftView(root):
    ans = []
    level = 0
    solve(root, ans, level)
    return ans



# Right View
def solve(root, ans, level):
    if root is None:
        return
    if level == len(ans):
        ans.append(root.data)
    solve(root.right, ans, level + 1)
    solve(root.left, ans, level + 1)



def LeftView(root):
    ans = []
    level = 0
    solve(root, ans, level)
    return ans




# Populating Next Right Pointers in each Node 
import queue
def populate(root):
    if root is None:
        return None
        
    qu = queue.Queue()
    qu.put(root)

    while not qu.empty():
        size = qu.qsize()
        prev = None

        for _ in range(size):
            curr = qu.get()
            curr.next = prev
            prev = curr

            if curr.right:
                qu.put(curr.right)

            if curr.left:
                qu.put(curr.left)
        
    return root



def connect(root):
    if root is None:
        return None
            
    qu = queue.Queue()
    qu.put(root)
    ans = []

    while not qu.empty():
        size = qu.qsize()
        prev = None

        for i in range(size):
            curr = qu.get()
            ans.append(curr)

            if curr.right:
                qu.put(curr.right)

            if curr.left:
                qu.put(curr.left)
            
        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]
        ans[-1].next = None
    
    return root
