# Sum of nodes on the longest path from root to leaf node

# Approach 1
def solve(root):
    if root is None:
        return (0, 0) # (sum, length)

    left = solve(root.left)
    right = solve(root.right)

    if left[1] < right[1]:
        return (root.data + right[0], right[1] + 1)
    elif left[1] > right[1]:
        return (root.data + left[0], left[1] + 1)
    else:
        return (root.data + max(left[0], right[0]), left[1] + 1)
    

def sumOfLongRootToLeafPath(root):
    return solve(root)[0]



# Love Babbar Solution 
def solve(root, curr_sum, maxSum, level, maxLevel):
    if root is None:
        if level > maxLevel[0]:
            maxLevel[0] = level
            maxSum[0] = curr_sum
        elif level == maxLevel[0]:
            maxSum[0] = curr_sum
        
        return 

    curr_sum += root.data
    solve(root.left, curr_sum, maxSum, level + 1, maxLevel)
    solve(root.right, curr_sum, maxSum, level + 1, maxLevel)
    

def sumOfLongRootToLeafPath(root):
    level = 0
    maxLevel = [0]
    curr_sum = 0
    maxSum = [float("-inf")]

    solve(root, curr_sum, maxSum, level, maxLevel)
    return maxSum[0]



# Sum of Right Leaf Nodes
# Sum of Left Leaf Nodes
# Next Right Node
