# Maximum of all subarrays of size k
from collections import deque

def maxSubarrays(arr, n, k):
    i = 0
    j = 0
    dq = deque()
    ans = []

    while j < n:
        if len(dq) == 0:
            dq.append(arr[j])
        else:
            while len(dq) > 0 and dq[-1] < arr[j]:
                dq.pop()
            dq.append(arr[j])
        
        if (j - i + 1) < k:
            j += 1
        
        elif (j - i + 1) == k:
            ans.append(dq[0])

            if arr[i] == dq[0]:
                dq.popleft()
        
            i += 1
            j += 1
    
    return ans
