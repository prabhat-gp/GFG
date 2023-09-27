# Reverse Descending Sorted Array

def binarySearch(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1



arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
n = len(arr)
key = 4
print(binarySearch(arr, n, key))
