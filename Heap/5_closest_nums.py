# Kth Closest Number (Lucy's Neighbors)

# Using Heap
import heapq as hq

def Kclosest(arr, n, k, x):
    heap = []
    ans = []
        
    for i in range(n):
        diff = abs(arr[i]-x)
        hq.heappush(heap, (diff, arr[i]))  

    while k > 0:
        ans.append(hq.heappop(heap)[1])
        k -= 1

    ans.sort()
    return ans

# arr = [10, 2, 14, 4, 7, 6]
arr = [-21, 21, 4, -12, 20]
n = len(arr)
x = 0
k = 4
print(Kclosest(arr, n, k, x))

# T.C = O(N + KlogK)
# S.C = O(N)


# 2 Pointer Approach
def Kclosest(arr, n, k, x):
    low = 0
    high = n - 1

    while high - low >= k:
        if abs(x - arr[low]) > abs(x - arr[high]):
            low += 1
        else:
            high -= 1
    
    return arr[low : high + 1]

# T.C = O(N)
# S.C = O(1)
