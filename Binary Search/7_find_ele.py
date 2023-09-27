# Find an Element in Rotated Sorted Array

def binarySearch(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


def findKRotations(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        if arr[low] <= arr[mid]:
            low = mid + 1
        elif arr[high] <= arr[mid]:
            high = mid - 1
        else:
            high -= 1
    
    return 0


def Search(arr, n, key):
    indx = findKRotations(arr,  n)
    temp1 = binarySearch(arr, 0, indx - 1, key)
    temp2 = binarySearch(arr, indx, n - 1, key)

    if temp1 == -1 and temp2 == -1:
        return -1
    elif temp1 == -1:
        return temp2
    else:
        return temp1


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr)
key = 10
print(Search(arr, n, key))
