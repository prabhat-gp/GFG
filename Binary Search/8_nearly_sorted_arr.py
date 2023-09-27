# Searching in Nearly Sorted Array

def search(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] == key and arr[mid - 1] >= low:
            return mid - 1
        elif arr[mid] == key and arr[mid + 1] <= high:
            return mid + 1
        elif arr[mid] > key:
            high = mid - 2
        elif arr[mid] < key:
            low = mid + 2
    
    return -1

arr = [5, 10, 30, 20, 40]
n = len(arr)
key = 40
print(search(arr, n, key))