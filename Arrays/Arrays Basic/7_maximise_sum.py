# Maximize sum(arr[i]*i) of an Array

def maximise(arr, n):
    arr.sort()
    maxSum = 0

    for i in range(n):
        maxSum = maxSum % 1000000007
        maxSum += (arr[i] * i) % 1000000007
    
    return maxSum % 1000000007

arr = [5, 3, 2, 4, 1]
n = len(arr)
print(maximise(arr, n))
