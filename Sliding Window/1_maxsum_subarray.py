# Max Sum Subarray of size K

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
