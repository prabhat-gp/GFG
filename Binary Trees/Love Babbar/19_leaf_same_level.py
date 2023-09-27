# Given a Binary Tree, check if all leaves are at same level or not.

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