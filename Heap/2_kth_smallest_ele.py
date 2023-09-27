# kth smallest element
import heapq

# Using Priority Queue (Not Optimal)
def kthSmallest(arr, n, k):
    hq = []
    for i in range(k):
        heapq.heappush(hq, arr[i])
        heapq._heapify_max(hq)
    
    for i in range(k, n):
        if arr[i] < hq[0]:
            heapq.heappop(hq)

            heapq.heappush(hq, arr[i])
            heapq._heapify_max(hq)
    
    return hq[0]

# Not passed all test cases


# Using map
def kthSmallest(arr, l, r, k):
    cnt = 0
    map = {}
    for ele in arr[l:r+1]:
        if ele in map:
            map[ele] += 1
        else:
            map[ele] = 1
    
    for num in sorted(map.keys()):
        cnt += map[num]
        if cnt >= k:
            return num





