# Postorder Traversal

# Recursive Approach
def traversal(root, res):
    if root is None:
        return 
    
    traversal(root.left, res)
    traversal(root.right, res)
    res.append(root.data)

def postOrder(root):
    res = []
    traversal(root, res)
    return res
   