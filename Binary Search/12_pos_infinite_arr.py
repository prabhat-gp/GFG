# Find position of element in an infinite sorted array

def binarySearch(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return  -1

def findPos(arr, key):
    low = 0
    high = 1

    while key > arr[high]:
        low = high
        high = high * 2

    binarySearch(arr, low, high, key)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
key = 14
print(findPos(arr, key))
