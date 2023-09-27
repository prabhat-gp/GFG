# Minimize the Heights I and Minimize the Heights II
# Minimise the maximum difference between 2 heights

# Height of the tower can't be negative
def getMinDiff(arr, n, k):
    arr.sort()
    minHeight = arr[0]
    maxHeight = arr[n - 1]
    diff = maxHeight - minHeight

    for i in range(1, n):
        if arr[i] < k:
            continue
        minHeight = min(arr[0] + k, arr[i] - k)
        maxHeight = max(arr[i - 1] + k, arr[n - 1] - k)
        currDiff = maxHeight - minHeight
        diff = min(diff, currDiff)

    return diff
    
arr = [12, 15, 6, 3, 5, 8]
n = len(arr)
k = 4
print(getMinDiff(arr, n, k))




# Height of the tower can be negative
def getMinDiff(arr, n, k):
    arr.sort()
    minHeight = arr[0]
    maxHeight = arr[n - 1]
    diff = maxHeight - minHeight

    for i in range(1, n):
        minHeight = min(arr[0] + k, arr[i] - k)
        maxHeight = max(arr[i - 1] + k, arr[n - 1] - k)
        currDiff = maxHeight - minHeight
        diff = min(diff, currDiff)

    return diff



