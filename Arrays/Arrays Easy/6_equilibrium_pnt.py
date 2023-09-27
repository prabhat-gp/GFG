# Equilibrium Point (1-based Indexing)

# Approach 1
def equilibriumPoint(arr, n):
    totalSum = sum(arr)
    leftSum = 0
    for i in range(n):
        if leftSum == totalSum - leftSum - arr[i]:
            return i + 1
        leftSum += arr[i]
    return -1


# Prefix Sum Approach
def equilibriumPoint(arr, n):
    if n == 1:
        return n
    
    totalSum = sum(arr)
    preSum = arr[0]
    
    for i in range(1, n - 1):
        preSum += arr[i]
        if preSum - arr[i] == (totalSum - preSum):
            return i + 1
    
    return -1

arr = [1, 3, 5, 2, 2]
n = len(arr)
print(equilibriumPoint(arr, n))
