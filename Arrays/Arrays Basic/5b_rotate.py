# Rotate the array to right by k steps
def solve(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

# Rotate Right
def rotateRight(arr, n, k):
    if k % n == 0:
        return
    k = k % n

    solve(arr, 0, n - k - 1)
    solve(arr, n - k, n - 1)
    solve(arr, 0, n - 1)
    return arr


# Rotate Left
def rotateLeft(arr, n, k):
    if k % n == 0:
        return
    k = k % n

    solve(arr, 0, k - 1)
    solve(arr, k, n - 1)
    solve(arr, 0, n - 1)
    return arr


# --------------------------------------------------

# Find k in Rotated Sorted Array = return mid
# 153. Find Minimum in Rotated Sorted Array = return arr[mid]

# Approach 1
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

# Approach: Index of array rotated = Index of min element
# ans = mid is smaller than both of its neighbours
# low to mid =  unsorted; mid to high = sorted


# Approach 2 (Only arr[mid], not index)
def findMin(arr, n):
    low = 0
    high = n - 1
    res = float("inf")

    while low <= high:
        mid = low + (high - low) // 2
        res = min(res, arr[mid])

        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
    return res



# --------------------------------------------------

# 189. Rotate Array (Left and Right)
# Find k in Rotated Sorted Array
# 153. Find Minimum in Rotated Sorted Array
# 154. Find Minimum in Rotated Sorted Array II
# 33. Search in Rotated Sorted Array
# 61. Rotate List 
# 2607. Make K-Subarray Sums Equal


# 189 -> 61,  2607
# 153 -> 33, 154