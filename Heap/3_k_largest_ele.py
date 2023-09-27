# Return k largest elements in array
import heapq 

def kLargest(arr, n, k):
    hq = []

    for i in range(n):
        heapq.heappush(hq, arr[i])
        if len(hq) > k:
            heapq.heappop(hq)
    
    return heapq.heappop(hq)

arr = [7, 10, 4, 3, 20, 15]
n = len(arr)
k = 3
print(kLargest(arr, n, k))


