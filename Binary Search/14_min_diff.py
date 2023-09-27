# Minimum Difference Element in a Sorted Array
# Given a sorted array, find the element in the array which has minimum difference with the given number. . 

def minDiff(arr, n, key):
    low = 0
    high = n - 1
    minDiff = float('inf')
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        diff = abs(arr[mid] - key)
        if diff < minDiff:
            minDiff = diff
            ans = arr[mid]
        if arr[mid] == key:
            return key
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return ans


# arr = [4, 6, 10]
arr = [1, 3, 8, 10, 15]
n = len(arr)
key = 12 # ans = 6
print(minDiff(arr, n, key))

