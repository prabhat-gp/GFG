class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.data})"

def buildTree():
    data = int(input("Enter the data to be inserted: "))

    if data == -1:
        return None
    
    root = Node(data)

    print("Enter left child of ", data)
    root.left = buildTree()

    print("Enter right child of ", data)
    root.right = buildTree()

    return root

# Inorder Traversal
def inOrder(root):
    if root is None:
        return 
    
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)


# Preorder Traversal
def preOrder(root):
    if root is None:
        return
    
    print(root.data, end = " ")
    preOrder(root.left)
    preOrder(root.right)

# Postorder Traversal
def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = " ")



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print("Inorder Traversal:")
    inOrder(root)
    print("\nPreorder Traversal:")
    preOrder(root)
    print("\nPostorder Traversal:")
    postOrder(root)


