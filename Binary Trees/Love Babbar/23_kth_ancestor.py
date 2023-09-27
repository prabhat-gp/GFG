# Kth Ancestor in a Tree

def solve(root, cnt, node, val):
    if root is None:
        return False
    
    if root.data == node:
        return True
    
    left = solve(root.left, cnt, node, val)
    right = solve(root.right, cnt, node, val)

    if left or right:
        cnt[0] -= 1
        if cnt[0] == 0:
            val[0] = root.data
        
        return True
    return False

def kthAncestor(root, k, node):
    cnt = [k]
    val = [-1]

    solve(root, cnt, node, val)
    return val[0]




# Approach 2 Using Map
def getParent(root, map):
    if root is None:
        return
    if root.left:
        map[root.left.data] = root
    if root.right:
        map[root.right.data] = root
    getParent(root.left, map)
    getParent(root.right, map)

def kthAncestor(root, k, node):
    if root is None:
        return -1

    map = {}
    getParent(root, map)
    map[root.data] = None
    ans = None

    for i in range(k):
        ans = map[node]
        if ans is None:
            return -1
        node = ans.data

    return ans.data