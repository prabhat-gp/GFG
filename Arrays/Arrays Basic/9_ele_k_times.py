# First element to occur k times

def firstElementKTime(arr, n, k):
    map = {}

    for i in range(n):
        map[arr[i]] = map.get(arr[i], 0) + 1
        if map[arr[i]] == k:
            return arr[i]
    
    return -1


arr = [1, 7, 4, 3, 4, 8, 7]
n = len(arr)
k = 2
print(firstElementKTime(arr, n, k))
