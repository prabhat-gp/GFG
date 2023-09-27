# Search an Element in Bitonic Array

def ascBinary(arr, low, high, key):

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def descBinary(arr, low, high, key):

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1



def peakEle(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        elif mid == 0:
            if n == 1 or arr[0] > arr[1]:
                return 0
            else:
                return 1
            
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
            else:
                return n - 2



def search(arr, n, key):
    peak = peakEle(arr, n)
    index1 = ascBinary(arr, 0, peak - 1, key)
    index2 = descBinary(arr, peak, n - 1, key)

    if index1 != -1:
        return index1
    else:
        return index2
    

arr = [1, 3, 8, 12, 4, 2]
n = len(arr)
key = 4
print(search(arr, n, key))
