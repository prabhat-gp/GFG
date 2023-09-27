# Top K Frequent Elements in Array 

# Approach 1
def topK(arr, n, k):
    map = {}
    temp = []
    ans = []

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    
    for key, value in map.items():
        temp.append((value, key))
    
    temp.sort()
    
    j = len(temp) - 1
    while k > 0:
        ans.append(temp[j][1])
        j -= 1
        k -= 1
    
    return ans

# T.C = O(NLogN)
# S.C = O(N)


# Using Heap
import heapq as hq

def topK(arr, n, k):
    map = {}
    heap = []
    ans = []

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    
    for key, value in map.items():
        hq.heappush(heap, (value, key))
        if len(heap) > k:
            hq.heappop(heap)

    for i in range(k):
        ans.append(hq.heappop(heap)[1])
    
    ans.reverse()
    return ans


arr = [1, 1, 1, 3, 2, 2, 4]
n = len(arr)
k = 2
print(topK(arr, n, k))




