# Kth smallest element

# Using map
def kthSmallest(arr, n, k):
    cnt = 0
    map = {}

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1

    for key, value in sorted(map.items()):
        cnt += value
        if cnt >= k:
            return key


# Using heap (Not done)
import heapq as hq

def kthSmallest1(arr, n, k):
    heap = []

    for i in range(k):
        hq.heappush(heap, arr[i])

    for i in range(k, n):
        if arr[i] < heap[0]:
            hq.heappop(heap)

            hq.heappush(heap, arr[i])

    return heap[0]

arr = [7, 10, 4, 3, 20, 15]
n = len(arr)
k = 3
print(kthSmallest1(arr, n, k))


# k largest elements

# Approach 1
def kLargest(arr, n, k):
    arr.sort()
    temp = []

    for i in range(n - 1, n - k - 1, -1):
        temp.append(arr[i])
    
    return temp

arr = [12, 5, 787, 1, 23]
n = len(arr)
k = 2




# Merge k Sorted Arrays
