# Number of Times a sorted array is rotated
# I/O = arr -> sorted -> rotated
# O/P = cnt

# Approach: Index of array rotated = Index of min element
# ans(mid) is smaller than both of its neighbours

def findKRotation(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n 
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        if arr[high] <= arr[mid]:
            high = mid - 1
        elif arr[low] <= arr[mid]: # low is in the sorted part, but ans is in unsorted part, so low = mid + 1
            low = mid + 1
        else: 
            high -= 1
    
    return 0



OrgArr = [2, 5, 6, 8, 11, 12, 15, 18]
arr = [11, 12, 15, 18, 2, 5, 6, 8]  # ans = 4
n = len(arr)
print(findKRotation(arr, n))

