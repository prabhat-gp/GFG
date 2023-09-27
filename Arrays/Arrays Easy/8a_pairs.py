# Count Pairs with given sum (2 Sum Problem) (Count Pairs Problem)

# Count Pairs (returns count)
def getPairsCount(arr, n, k):
    map = {}
    cnt = 0
    for i in range(n):
        temp = k - arr[i]
        if temp in map:
            cnt += map[temp]
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    return cnt

# T.C = O(N)
# S.C = O(N)

# Return indices
def twoSum(arr, n, k):
    map = {}
    for i in range(n):
        temp = k - arr[i]
        if temp in map:
            return {map[temp], i}
        map[arr[i]] = i
    return {}
        

# ------------------------------------------------------------------------------------------------------------------------

# Count Pairs (return count)
# Count Pairs (T/F)
# All Pairs given sum



# Count pairs with given sum (return count)
# Key Pair (return T/F)
# Find all pairs with a given sum (return pairs)
# Count distinct pairs with difference k
# Pair with given sum in a sorted array

