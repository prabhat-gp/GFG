# Maximum of all subarrays of size k (Sliding Window)

# Brute Force
def maxSumSubArray(arr, n ,k):
    i = 0
    j = 0
    maxSum = float("-inf")

    for i in range(n - k + 1):
        currSum = 0
        for j in range(i, i + k):
            currSum += arr[j]
        
        maxSum = max(maxSum, currSum)
    
    return maxSum


# Optimal
def maxSumSubArray(arr, n ,k):
    i = 0
    j = 0
    currSum = 0
    maxSum = float("-inf")

    while j < n:
        currSum += arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            maxSum = max(currSum, maxSum)
            currSum -= arr[i]
            i += 1
            j += 1
    
    return maxSum

# Sliding Window
from collections import deque

def maxSumSubArray(arr, n, k):
    i = 0
    j = 0
    ans = []
    dq = deque()

    while j < n:
        if len(dq) == 0:
            dq.append(arr[j])
        else:
            while len(dq) > 0 and dq[-1] < arr[j]:
                dq.pop()
            dq.append(arr[j])
        
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            ans.append(dq[0])

            if arr[i] == dq[0]:
                dq.popleft()
            
            i += 1
            j += 1
    return ans


