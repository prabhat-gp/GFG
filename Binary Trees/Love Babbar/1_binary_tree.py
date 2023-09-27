class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        # Helper function to print the tree in a readable format
        return f"Node({self.data})"


def buildTree():
    data = int(input("Enter the data for the current node (-1 for no node): "))

    if data == -1:
        return None

    root = Node(data)

    print("Enter left child of", data)
    root.left = buildTree()

    print("Enter right child of", data)
    root.right = buildTree()

    return root


if __name__ == "__main__":
    root = buildTree()
    print(root)


# Iterative Approach
def buildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root


def main():
    root = buildTree()

    print("Inorder Traversal:")
    inorderTraversal(root)


def inorderTraversal(node):
    if node is not None:
        inorderTraversal(node.left)
        print(node.data, end=" ")
        inorderTraversal(node.right)


if __name__ == "__main__":
    main()




# Recursive Approach
def buildTree(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(arr[mid])

    root.left = buildTree(arr, start, mid - 1)
    root.right = buildTree(arr, mid + 1, end)

    return root


def main():
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    root = buildTree(sorted_array, 0, len(sorted_array) - 1)

    print("Inorder Traversal:")
    inorderTraversal(root)


def inorderTraversal(node):
    if node is not None:
        inorderTraversal(node.left)
        print(node.data, end=" ")
        inorderTraversal(node.right)


if __name__ == "__main__":
    main()


