# Pre Order Traversal

# Recursive Approach
def traversal(root, res):
    if root is None:
        return 
    
    res.append(root.data)
    traversal(root.left, res)
    traversal(root.right, res)

def preorder(root):
    res = []
    traversal(root, res)
    return res
   

# Morris Traversal
def preOrder(root):
    res = []
    curr = root
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right:
                pred = pred.right
            pred.right = curr.right
            curr.right = curr.left
            curr.left = None  # Set the left subtree to None
        
        res.append(curr.data)
        curr = curr.right
    
    return res