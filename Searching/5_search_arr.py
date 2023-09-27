# Find Pivot Element
# Search in a Rotated Sorted Array

def getPivot(arr, n):
    low = 0
    high = n - 1

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] >= arr[0]:
            low = mid + 1
        else:
            high = mid
        
    return low

arr = [3, 8, 10, 17, 1]
n = len(arr)
print(getPivot(arr, n))



def binarySearch(arr, low, high, key):
    
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1 
    
    return -1


def search(arr, low, high, key):
    n = len(arr)
    pivot = getPivot(arr, n)

    if key >= arr[pivot] and key <= arr[n - 1]:
        return binarySearch(arr, pivot, n - 1, key)
    else:
        return binarySearch(arr, 0, pivot, key)
    
# T.C = O(logN)



# Minimum element in a sorted and rotated array
def findMinEle(arr, n):
    low = 0
    high = n - 1

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return arr[low]
 
arr = [4, 5, 1, 2, 3]
n = len(arr)
print(findMinEle(arr, n))