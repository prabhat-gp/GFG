# Given two binary trees, check if S is present as subtree in T. 

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None and root2 is not None:
        return False
    elif root1 is not None and root2 is None:
        return False
    
    left = isIdentical(root1.left, root2.left)
    right = isIdentical(root1.right, root2.right)

    value = root1.data == root2.data

    return left and right and value

def isSubTree(tree, subtree):
    if subtree is None:
        return True
    if tree is None:
        return False
    
    if isIdentical(tree, subtree):
        return True
    
    left = isSubTree(tree.left, subtree)
    right = isSubTree(tree.right, subtree)

    return left or right

