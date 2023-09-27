# Frequency Sort (Not Done)
import heapq as hq

def frequencySort(arr, n):
    map = {}
    heap = []
    

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    
    for key, value in map.items():
        hq.heappush(heap, (value, key))
    
    z = len(heap)
    ans = [1] * z
    i = 0
    while heap:
        ans[i] = hq.heappop(heap)[1]
        i += 1
    ans.reverse()
    
    return ans

arr = [1, 1, 1, 3, 2, 2, 4]
n = len(arr)
print(frequencySort(arr, n))