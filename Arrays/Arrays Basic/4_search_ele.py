# Search an Element in an array
def search(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
    
    return -1

# T.C = O(N)
# S.C = O(1)




# Searching an element in a sorted array
def binarySearch(arr, n, key):
    low = 0
    high  = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return False

def searchInSorted(arr, n, k):
    return binarySearch(arr, n, k)

# T.C = O(NlogN)
# S.C = O(N)
