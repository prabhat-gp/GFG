# Sort a k sorted Array (Nearly Sorted Array)

import heapq as hq

def nearlySorted(arr, n, k):
    min_heap = []
    ans = []

    for i in range(n):
        hq.heappush(min_heap, arr[i])
        if len(min_heap) > k:
            ans.append(hq.heapppop(min_heap))

    while min_heap:
        ans.append(hq.heappop(min_heap))

    return ans

# T.C = O(NlogK)
# S.C = O(N)
