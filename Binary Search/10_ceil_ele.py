# Find ceil of an element in Sorted Array (No Duplicates)

# Ceil of key = Smallest element greater than key

def findCeil(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            res = mid
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
    
    return res
        

arr1 = [1, 2, 8, 10, 11, 12, 19]
n1 = len(arr1)
key = 5 # ans = 2
print(findCeil(arr1, n1, key))

arr2 = [1, 2, 3, 4, 8, 10, 12, 19]
n2 = len(arr2)
y = 9 # ans = 5
print(findCeil(arr2, n2, y))
 

