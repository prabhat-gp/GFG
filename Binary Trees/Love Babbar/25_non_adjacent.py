# Maximum sum of Non-adjacent nodes

def solve(root):
    if root is None:
        return (0, 0)

    left = solve(root.left) if root.left else (0, 0)
    right = solve(root.right) if root.right else (0, 0)

    without = max(left[0] + right[0], left[0] + right[1], left[1] + right[0], left[1] + right[1])
    with_current = root.data + left[1] + right[1]

    return (with_current, without)

def getMaxSum(root):
    ans = solve(root)

    return max(ans[0], ans[1])



def solve(root):
    if root is None:
        return (0, 0)

    left = solve(root.left)
    right = solve(root.right)

    ans = (root.data + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))

    return ans

def getMaxSum(root):
    ans = solve(root)

    return max(ans[0], ans[1])

# T.C: O(Number of nodes in the tree).
# Aux Space: O(Height of the Tree).




# Maximum difference between node and its ancestor