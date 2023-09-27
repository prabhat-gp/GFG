# Cyclically rotate an array by one
# Move last element to first Index
def rotate(arr, n):
    temp = arr[-1]
    
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i-1]
    
    arr[0] = temp
    return arr

arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rotate(arr, n))


# ---------------------------------------------------------------------------------------------------------------------------


# Rotate Array by d places
def rotate(arr, start, end):
    l = start
    r = end
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def rotateArr(arr, n, d):
    if d % n == 0:
        return
    else:
        d = d % n
    rotate(arr, 0, d - 1)
    rotate(arr, d, n - 1)
    rotate(arr, 0, n - 1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
d = 2
print(rotateArr(arr, n, d))


# ---------------------------------------------------------------------------------------------------------------------------


# Right Rotated array by k places. Find k
# Number of Times a sorted array is rotated
# I/O = arr -> sorted -> rotated
# O/P = cnt

# Approach: Index of array rotated = Index of min element
# ans(mid) is smaller than both of its neighbours
# low to mid =  unsorted; mid to high = sorted

def findKRotation(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n 

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] >= arr[high]:
            low = mid + 1
        elif arr[mid] <= arr[low]:
            high = mid - 1
        else:
            high -= 1
        
    return 0


OrgArr = [2, 5, 6, 8, 11, 12, 15, 18]
arr = [11, 12, 15, 18, 2, 5, 6, 8]  # ans = 4
n = len(arr)
print(findKRotation(arr, n))

# T.C = O(logN)
# S.C = O(1)


# ---------------------------------------------------------------------------------------------------------------------------

# 