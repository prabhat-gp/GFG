def maxSubArraySum(arr, n):
    maxSum = arr[0]
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

