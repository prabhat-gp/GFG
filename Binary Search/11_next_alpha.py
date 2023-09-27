# Next Alphabetical Element (Similar to Ceil)

def nextAlpha(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            low = mid + 1
        elif arr[mid] > key:
            res = mid
            high = mid - 1
        elif arr[mid] < key:
            low  = mid + 1
    
    return res


arr = ['a', 'c', 'f', 'h']
n = len(arr)
key = 'f'
print(nextAlpha(arr, n, key))

