

def firstOcc(arr, n, key):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            ans = mid
            high = mid - 1

        elif arr[mid] > key:
            high = mid - 1

        else:
            low = mid + 1
    
    return ans

def lastOcc(arr, n, key):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            ans = mid
            low = mid + 1

        elif arr[mid] > key:
            high = mid - 1

        else:
            low = mid + 1
    
    return ans

def count(arr, n, key):
    first = firstOcc(arr, n, key)
    last = lastOcc(arr, n, key)

    if first == -1 and last == -1:
        return 0
    else:
        return last - first + 1

