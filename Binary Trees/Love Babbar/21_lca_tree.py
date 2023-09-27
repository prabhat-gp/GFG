# Lowest Common Ancestor in Binary Tree

def lca(root, n1, n2):
    if root is None:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    leftAns = lca(root.left, n1, n2)
    rightAns = lca(root.right, n1, n2)

    if leftAns is not None and rightAns is not None:
        return root
    elif leftAns is not None and rightAns is None:
        return leftAns
    elif leftAns is None and rightAns is not None:
        return rightAns
    else:
        return None
    
# T.C  = O(N)
# S.C = O(height)


# Maximum difference between node and its ancestor
# Maximum path sum from any node