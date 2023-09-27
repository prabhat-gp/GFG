# Create Tree from Level Order Traversal
import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.data})"
    
def buildFromLevelOrder():
    data = int(input("Enter the data for root node (-1 for no node): "))

    if data == -1:
        return None
    
    root = Node(data)
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current = q.get()
        
        left_data = int(input(f"Enter left child of {current.data} (-1 for no node): "))
        if left_data != -1:
            current.left = Node(left_data)
            q.put(current.left)

        right_data = int(input(f"Enter right child of {current.data} (-1 for no node): "))
        if right_data != -1:
            current.right = Node(right_data)
            q.put(current.right)

    return root

def inOrder(root):
    if root is None:
        return 
    
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)



if __name__ == "__main__":
    root = buildFromLevelOrder()


    print("Inorder Traversal")
    inOrder(root)



# Count Leaf Nodes in Binary Tree (Preorder Traversal)
def countLeaves(root):
    if root is None:
        return 0
        
    if root.left is None and root.right is None:
        return 1
    leftCount = countLeaves(root.left)
    rightCount = countLeaves(root.right)
    
    return leftCount + rightCount
