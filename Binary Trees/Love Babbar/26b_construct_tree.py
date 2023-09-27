# Construct Tree from Inorder & Postorder

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPosition(inorder, inorderStart, inorderEnd, element):
    for i in range(inorderStart, inorderEnd + 1):
        if inorder[i] == element:
            return i
    return -1

def solve(inorder, postorder, postorderIndex, inorderStart, inorderEnd):
    if postorderIndex[0] < 0 or inorderStart > inorderEnd: # change
        return None

    element = postorder[postorderIndex[0]]
    root = Node(element)
    position = findPosition(inorder, inorderStart, inorderEnd, element)

    postorderIndex[0] -= 1 # change
    root.right = solve(inorder, postorder, postorderIndex, position + 1, inorderEnd) # reverse
    root.left = solve(inorder, postorder, postorderIndex, inorderStart, position - 1)
    
    return root

def buildTree(inorder, postorder, n):
    postorderIndex = [n - 1] # change
    ans = solve(inorder, postorder, postorderIndex, 0, n - 1)
    return ans



# T.C = O(N^N)
# S.C = O(N)




