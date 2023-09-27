# Construct Tree from Inorder & Preorder

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

def solve(inorder, preorder, preorderIndex, inorderStart, inorderEnd):
    n = len(inorder)
    if preorderIndex[0] >= n or inorderStart > inorderEnd:
        return None

    element = preorder[preorderIndex[0]]
    root = Node(element)
    position = findPosition(inorder, inorderStart, inorderEnd, element)

    preorderIndex[0] += 1
    root.left = solve(inorder, preorder, preorderIndex, inorderStart, position - 1)
    root.right = solve(inorder, preorder, preorderIndex, position + 1, inorderEnd)

    return root

def buildTree(inorder, preorder, n):
    preorderIndex = [0]
    ans = solve(inorder, preorder, preorderIndex, 0, n - 1)
    return ans


# T.C = O(N^N)
# S.C = O(N)

