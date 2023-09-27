# Iterative Code

def binarySearch(arr, n, x):
    low = 0
    high = n - 1

    while low <= high: # important
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return 1
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
        
    return -1

arr = [3, 4, 6, 7, 9, 12, 16, 17]
n = len(arr)
x = 6
print(binarySearch(arr, n, x))

# T.C = O(logN)
 

# Using Recursion
def binarySearch(arr, low, high, x):
    if low > high:
        return False
    
    mid = low + (high - low) // 2
    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return binarySearch(arr, low, mid - 1, x)
    else:
        return binarySearch(arr, mid + 1, high, x)


arr = [3, 4, 6, 7, 9, 12, 16, 17]
n = len(arr)
x = 5
print(binarySearch(arr, 0, n - 1, x))



# Approach
def binarySearch(arr, n, key):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid]  > key:
            high = mid - 1
        else:
            low = mid + 1 
    
    return -1


# Lower bound, Upper bound, No of Occurences, Pivot Element, Search in Rotated Array, 
# Search in smaller space (Agg Cows, ROTI, PRATA, Book Allocation problem)



# Searching and Sorting -> Binary Trees -> Binary Search Trees -> Graphs -> Strings