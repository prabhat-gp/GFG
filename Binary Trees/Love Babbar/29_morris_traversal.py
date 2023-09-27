# Morris Traversal

# Flatten binary tree to linked list (Preorder Traversal)
def flatten(root):
    curr = root
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right:
                pred = pred.right
            pred.right = curr.right
            curr.right = curr.left
            curr.left = None  # Set the left subtree to None
        
        curr = curr.right
    
    return root



