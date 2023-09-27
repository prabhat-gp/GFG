# Given a Binary Tree, convert it into its mirror.

def mirror(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        return
    
    mirror(root.left)
    mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp


# Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.
def function(root, left, right):
    if root is None:
        return True
    
    if left is None or right is None or left.data != right.data:
        return False
    
    return function(left.left, right.right) and function(left.right, right.left)

def isSymmetric(root):
    if root is None:
        return True
    
    return function(root.left, root.right)



# Approach 2
def isMirror(self, left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    
    return (left.data == right.data) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
def isSymmetric(self, root):
    if not root:
        return True
    
    return self.isMirror(root.left, root.right)


# Approach 3
def Symmetric(self, root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.data != root2.data:
        return False
    else:
        ls = self.Symmetric(root1.left, root2.right)
        rs = self.Symmetric(root1.right, root2.left)
        return ls and rs
    
def isSymmetric(self, root):
    return self.Symmetric(root, root)
