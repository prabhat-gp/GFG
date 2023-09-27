# Order not Known (Order Agnostic Search)
# Not known whether is ascending or descending

def binarySearch(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[low] < arr[high]:
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1




# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = [5]
n = len(arr)
key = 5
print(binarySearch(arr, n, key))  