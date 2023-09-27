# Count of an Element in a Sorted Array (Count Occurences)

def firstOcc(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            res = mid
            high = mid - 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return res

def lastOcc(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            res = mid
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return res 

def find(arr, n, key):
    first = firstOcc(arr, n, key)
    last = lastOcc(arr, n, key)

    if first == -1 and last == -1:
        return 0
    else:
        return last - first + 1



arr = [2, 4, 10, 10, 10, 18, 20]
n = len(arr)
key = 10
print(find(arr, n, key))
# mid = 2, 4; len = 3
