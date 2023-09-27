# Find the index of 1st 1 in a Infinite Binary Sorted Array

def firstOcc(arr, low, high, key):
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


def firstIndex(arr, key):
    low = 0
    high = 1

    while key > arr[high]:
        low = high
        high = high * 2

    return firstOcc(arr, low, high, key)
