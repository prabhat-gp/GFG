# Kadane's Algorithm (Largest sum contiguous subarray)

# Brute Force
def maxSubArraySum(arr, n):
    ans = float("-inf")

    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += arr[j]
            ans = max(ans, currSum)
    return ans

# Optimal
def maxSubArraySum(arr, n):
    maxSum = float("-inf")
    curSum = 0
        
    for i in range(0, n):
        curSum = curSum + arr[i]
        if curSum > maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0
    return maxSum

arr = [1, 2, 3, -2, 5]
n = len(arr)
print(maxSubArraySum(arr, n))



# Smallest sum contiguous subarray
def smallestSumSubarray(arr, n):
    minSum = float("inf")
    currSum = 0
    for i in range(0, n):
        currSum += arr[i]
        if currSum <  minSum:
            minSum = currSum
        if currSum > 0:
            currSum = 0
    
    return minSum




# Maximum Sub Array
def findSubarray(arr, n):
    currSum = 0
    maxSum = arr[0]
    start = 0
    end = 0
    s = 0

    for i in range(n):
        currSum += arr[i]
        if currSum > maxSum:
            maxSum = currSum
            start = s
            end = i
        
        if currSum < 0:
            currSum = 0
            s = i + 1
    
    return arr[start:end + 1]

arr = [1, 2, 3, -2, 5]
arr = []
n = len(arr)
print(findSubarray(arr, n))

