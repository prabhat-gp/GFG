# Determine if Two Trees are Identical

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
