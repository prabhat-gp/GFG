# Inorder Traversal

# Recursive Approach
def traversal(root, res):
    if root is None:
        return
    
    traversal(root.left, res)
    res.append(root.data)
    traversal(root.right, res)

def inorder(root):
    res = []
    traversal(root, res)
    return res



# Morris Traversal
def inOrder(root):
    res = []
    curr = root
    while curr:
        if curr.left is None:
            res.append(curr.data)
            curr = curr.right
        else:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
                
            if pred.right is None:
                    pred.right = curr
                    curr = curr.left
            else:
                pred.right = None
                res.append(curr.data)
                curr = curr.right
    return res

