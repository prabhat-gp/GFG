# Find pair with a given Difference

# Brute Force
def findPair(arr, n, k):
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) == k:
                return True
    
    return False

# T.C = O(N^2) 
# S.C = O(1)



# Using Binary Search
def binarySearch(arr, low, high, k):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return True
        if arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
        
    return False


def findPair(arr, n, k):
    arr.sort()
    target = -1

    for i in range(0, n):
        target = arr[i] + k
        if target > arr[n - 1]:
            continue
        else:
            if binarySearch(arr, i + 1, n - 1, target):
                return True
    
    return False

arr = [1, 3, 5, 8, 10]
n = len(arr)
k = 5
print(findPair(arr, n, k))



# Using Map
def findPair(arr, n, k):
    map = {}
    target = -1

    for i in range(0, n):
        map[arr[i]] = i
    
    for i in range(0, n):
        target = arr[i] + k
        if target in map and map[target] != i:
            return True
    
    return False

# T.C = O(N) 
# S.C = O(N)



