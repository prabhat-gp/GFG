# First and last occurrences of x

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

def find(arr, n, key):
    first = firstOcc(arr, n, key)
    last = lastOcc(arr, n, key)

    return first, last


arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
n = len(arr)
key = 5

print(find(arr, n, key))
