# Height of Binary Tree (Depth)
# Height = Longest path between root node and a leaf node

class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root): 
    if root is None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    ans = max(left, right) + 1
    return ans

# T.C = O(N)
# S.C = O(height)
# Worst Case = O(N)


# Minimum Depth of Binary Tree
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