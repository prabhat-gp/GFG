# Check for Balanced Tree
# A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Brute Force
def height(root):
    if root is None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    ans = max(left, right) + 1
    return ans

def isBalanced(root):
    if root is None:
        return True
    
    left = isBalanced(root.left)
    right = isBalanced(root.right)

    diff = abs(height(root.left) - height(root.right)) <= 1

    if left and right and diff:
        return True
    else:
        return False

# T.C = O(N^2)


# Optimal
def balanceFast(root):
    if root is None:
        return (True, 0)

    left = balanceFast(root.left)
    right = balanceFast(root.right)
    ans = (False, 0)

    if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
        ans = (True, max(left[1], right[1]) + 1)

    return ans

def isBalanced(root):
    return balanceFast(root)[0]

# (left[0], left[1]) = (isBalanced, height) = (bool, int) 