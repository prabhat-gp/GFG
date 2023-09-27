# Binary Search
# "sorted" keyword -> Binary Search -> reduce T.C

def binarySearch(arr, n, key):
    low = 0
    high  = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1, 2, 3, 4, 5]
n = len(arr)
key = 3
print(binarySearch(arr, n , key))


# Binary Search is used to reduce search space. In case of linear search, as the length of array increases it's not feasible.