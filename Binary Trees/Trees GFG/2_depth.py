# Height of Binary Tree (Max Depth)
def height(root):
    if root is None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    ans = max(left, right) + 1
    return ans



# Min Depth of Binary Tree
def minDepth(root) :
    if root is None:
        return 0
    
    left = minDepth(root.left)
    right = minDepth(root.right)

    if left == 0:
        return right + 1
    if right == 0:
        return left + 1

    ans = min(left, right) + 1
    return ans



# Max Depth of N-ary Tree
def maxDepth(root):
    if root is None:
        return 0
    
    depth = 1
    for node in root.children:
        curr = maxDepth(node) + 1
        depth = max(depth, curr)
    return depth




# Leaf Nodes at same level
def height(root): 
    if root is None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    ans = max(left, right) + 1
    return ans

def minDepth(root):
    if root is None:
        return 0
    
    left  = minDepth(root.left)
    right = minDepth(root.right)

    if left == 0:
        return right + 1
    if right == 0:
        return left + 1
    
    ans = min(left, right) + 1
    return ans

def check(root):
    max_depth = height(root)
    min_depth = minDepth(root)

    return max_depth == min_depth


# Height of BT
# Min Depth of BT
# Balanced BT
# Max Depth of N-ary Tree