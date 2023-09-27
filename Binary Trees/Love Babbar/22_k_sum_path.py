# Given a binary tree and an integer K. Find the number of paths in the tree which have their sum equal to K.

# Love Babbar (Not passed all test cases)
def result(root, k, cnt, path):
    if root is None:
        return
    
    path.append(root.data)

    result(root.left, k, cnt, path)
    result(root.right, k, cnt, path)

    currSum = 0
    n = len(path)
    for i in range(n - 1, -1, -1):
        currSum += path[i]
        if currSum == k:
            cnt[0] += 1
    
    path.pop()

def sumK(root, k):
    path = []
    cnt = [0] # # Using a list to mimic a reference for 'count'
    result(root, k, cnt, path)
    return cnt[0]

# T.C = O(N^2)

# Using map
def solve(root, k, cnt, map, prevSum):
    if root is None:
        return
    
    currSum = root.data + prevSum

    if currSum - k in map:
        cnt[0] += map[currSum - k]

    if currSum == k:
        cnt[0] += 1

    map[currSum] = map.get(currSum, 0) + 1 # if currSum -> currSum else 0

    solve(root.left, k, cnt, map, currSum)
    solve(root.right, k, cnt, map, currSum)

    map[currSum] -= 1

def sumK(root, k):
    map = {}
    cnt = [0]
    solve(root, k, cnt, map, 0)
    return cnt[0]

# T.C = O(N)
