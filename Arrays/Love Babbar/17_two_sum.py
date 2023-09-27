# Count Pairs with given sum (2 Sum Problem) (Count Pairs Problem)

# Count Pairs (return count)
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


# -----------------------------------------------------------------------------------------------------------------------


# Check if pair with given sum exists in Array (Key Pair)

# Count Pairs (return T/F)
# Brute Force 
def twoSum(arr,n, k):
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                # return True
                return [i, j]
    # return False
    return[]

# Time limit Exceeded T.C = O(N2)



# 2 Pointer Approach
def twoSum(arr, n, k):
    arr.sort()
    low = 0
    high = n - 1

    while low < high:
        total = arr[low] + arr[high]
        
        if total > k:
            high -= 1
        elif total < k:
            low += 1
        else:
            return True

    return False

# Time limit Exceeded T.C = O(NlogN) 
# S.C = O(1)



# Using map
def twoSum(arr, n, k):
    map = {}

    for i in range(0, n):
        temp = k - arr[i]
        if (temp in map):
            return True
            # return [map[temp], i]
        map[arr[i]] = i

    return False
    # return []


# T.C = O(N) 
# S.C = O(N)



arr = [2, 6, 5, 8, 11]
n = len(arr)
k = 14
print(twoSum(arr, n, k))



