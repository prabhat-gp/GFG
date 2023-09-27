# Check Subtree (Subtree of another tree)
def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
        
    if root1 is None or root2 is None:
        return False
        
    if root1.data != root2.data:
        return False
            
    x = isIdentical(root1.left, root2.left)
    y = isIdentical(root1.right, root2.right)
        
    return x and y

def isSubtree(tree, subRoot):
    if subRoot is None:
        return True
            
    if tree is None:
        return False
            
    if isIdentical(tree, subRoot):
        return True
        
    left = isSubtree(tree.left, subRoot)
    right = isSubtree(tree.right, subRoot)
        
    return left or right






# Most Frequent Subtree Sum
def subtreeSum(root, map):
    if root is None:
        return 0
    
    sum = root.data + subtreeSum(root.left, map) + subtreeSum(root.right, map)
    map[sum] = map.get(sum, 0) + 1
    return sum


def findFrequentTreeSum(root):
    if root is None:
        return []
    
    map = {}
    subtreeSum(root, map)
    
    max_freq = max(map.values())
    res = []
    for data, freq in map.items():
        if max_freq == freq:
            res.append(data)
            
    return res
