# Smallest subarray with sum greater than k

# Brute Force
def smallestSubWithSum(arr, n, k):
    cnt = float('inf')
    
    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += arr[j]
            if currSum > k:
                cnt = min(cnt, j - i + 1)

    if cnt != float('inf'):
        return cnt
    else:
        return 0



# Approach 2
def smallestSubWithSum(arr, n, k):
    low = 0
    high = 0
    currSum = 0
    res = float("inf")

    for i in range(n):
        currSum += arr[i]

        while low <= high and currSum > k:
            res = min(res, high - low + 1)
            currSum -= arr[low]
            low += 1
        high += 1

    if res != float("inf"):
        return res
    else:
        return 0



# Optimal Approach (Sliding Window)
def smallestSubWithSum(arr, n, k):
    low = 0
    high = 0
    currSum = arr[0]
    cnt = float('inf')
    
    while high < n and low < n:
        if currSum <= k:
            high += 1
            if high < n:
                currSum += arr[high]
        else:
            cnt = min(cnt, high - low + 1)
            currSum -= arr[low]
            low += 1
    
    if cnt == float('inf'):
        return 0
    
    return cnt




arr = [1, 4, 45, 6, 0, 19]
n = len(arr)
k = 51
print(smallestSubWithSum(arr, n, k))
