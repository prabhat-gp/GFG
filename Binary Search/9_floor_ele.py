# Find floor of an element in Sorted Array (No Duplicates)

# Floor of key = Greatest element smaller than key
def findFloor(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            res =  mid
            low = mid + 1
    
    return res
        

arr1 = [1, 2, 8, 10, 11, 12, 19]
n1 = len(arr1)
key1 = 5 # ans = 1
print(findFloor(arr1, n1, key1))

arr2 = [1, 2, 3, 4, 8, 10, 12, 19]
n2 = len(arr2)
y = 8 # ans = 4
print(findFloor(arr2, n2, y))







