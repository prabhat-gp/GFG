# Find Transition Point

# Brute Force
def transitionPoint(arr, n):
    for i in range(n):
        if arr[i] == 1:
            return i
    
    return -1

# T.C = O(N)




# Binary Search Approach
def binarySearch(arr, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
            return mid
        elif arr[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def transitionPoint(arr, n):
    left = 0
    right = n - 1
    return binarySearch(arr, left, right)


arr = [0,0,0,1,1]
n = len(arr)
print(transitionPoint(arr, n))

# T.C = O(logN)
