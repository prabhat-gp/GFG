# Path Sum
# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# Approach 1
def checkSum(root, k, currSum):
    if root is None:
        return True
    
    if root.left is None or root.right is None:
        currSum += root.data
        if currSum == k:
            return True
    
    left = checkSum(root.left, k, currSum + root.data)
    right = checkSum(root.right, k, currSum + root.data)

    return left or right

def hasPathSum(root, k):
    currSum = 0
    return checkSum(root, k, currSum)



# Approach 2
def isPathTreeFast(root, k):
    if root is None:
        return (False, 0)
    
    if root.left is None and root.right is None:
        return (root.data == k, root.data)
    
    left = isPathTreeFast(root.left, k - root.data)
    right = isPathTreeFast(root.right, k - root.data)

    ans = (False, 0)

    if left[0] or right[0]:
        ans = (True, root.val + left[1] + right[1])
        
    return ans

def hasPathSum(root, k):
    return isPathTreeFast(root, k)[0]






# -----------------
# Path Sum II (DFS)

# Approach 1
def findSumPaths(root, k, currPath):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        if root.data == k:
            return [currPath + [root.data]]
        else:
            return []
    
    left = findSumPaths(root.left, k - root.data, currPath + [root.data])
    right = findSumPaths(root.right, k - root.data, currPath + [root.data])

    return left + right

def pathSum(root, k):
    return findSumPaths(root, k, [])






# -----------------
# Path Sum III (DFS)

# Approach 1
def countPaths(root, k, currSum):
    if root is None:
        return 0
    
    currSum += root.data
    cnt = 0
    if currSum == k:
        cnt += 1

    cnt += countPaths(root.left, k, currSum)
    cnt += countPaths(root.right, k, currSum)

    return cnt

def pathSum(root, k):
    if root is None:
        return 0
    
    x = countPaths(root, k, 0)
    left = pathSum(root.left, k)
    right = pathSum(root.right, k)

    return x + left + right



# Optimal
def solve(root, k, currSum, map):
    if root is None:
        return 0
    
    currSum += root.data
    cnt = 0
    if currSum - k in map:
        cnt += map[currSum  - k]

    map[currSum] = map.get(currSum, 0) + 1
    left = solve(root.left, k, currSum, map)
    right = solve(root.right, k, currSum, map)
    map[currSum] -= 1

    return left + right + cnt


def pathSum(root, k):
    map = {0 : 1} # Initialize the map with {0: 1} to handle the case where current sum is equal to k
    return solve(root, k, 0, map)






# -----------------
# Longest Univalue Path

def path(root, ans, prev = -1):
    if not root:
        return 0
    
    left = path(root.left, ans, root.val)
    right = path(root.right, ans, root.val)
    ans[0] = max(ans[0], right + left)
    
    if root.val != prev:
        return 0
    
    return max(right, left) + 1

def longestUnivaluePath(root):
    ans = [0]  # Using a list to simulate pass-by-reference behavior
    path(root, ans)
    return ans[0]

