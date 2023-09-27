# First negative integer in every window of size “k”

# Brute Force
def printFirstNegativeInteger(arr, n, k):
    result = []

    for i in range(n - k + 1):
        flag = False

        for j in range(k):
            if arr[i + j] < 0:
                result.append(arr[i + j])
                flag = True
                break

        if not flag:
            result.append(0)

    return result




# Approach 2 (Not Optimal Solution)
from collections import deque
def printFirstNegativeInteger(arr, n, k):
    result = []
    dq = deque()

    for i in range(k):
        if arr[i] < 0:
            dq.append(i)

    if dq:
        result.append(arr[dq[0]])
    else:
        result.append(0) 

    for i in range(k, n):
        while dq and dq[0] <= i - k:
            dq.popleft()

        if arr[i] < 0:
            dq.append(i)

        if dq:
            result.append(arr[dq[0]])
        else:
            result.append(0) 

    return result