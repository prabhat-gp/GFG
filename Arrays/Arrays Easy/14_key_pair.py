# Check if pair with given sum exists in Array (Key Pair)

# Count Pairs (T/F)
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


# ------------------------------------------------------------------------------------------------------------------------


# Pair with given sum in a sorted array
def Countpair(arr, n, k):
    low = 0
    high = n - 1
    cnt = 0

    while low < high:
        total = arr[low] + arr[high]
        if total == k:
            cnt += 1
            low += 1
            high -= 1
        elif total > k:
            high -= 1
        elif total < k:
            low += 1

    if cnt == 0:
        return -1
    else:
        return cnt



arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 8

# T.C = O(N)
# S.C = O(1)