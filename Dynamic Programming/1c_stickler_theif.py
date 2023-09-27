# Stickler Thief





# Using Tabulation
def FindMaxSum(arr, n):
    dp = [0] * n

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
    
    return dp[n - 1]

arr = [6, 5, 5, 7, 4]
n = len(arr)
print(FindMaxSum(arr, n))



# Using DP
def FindMaxSum(arr, n):
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    
    first = arr[0]
    second = max(arr[0], arr[1])
        
    for i in range(2, n):
        temp = max(first + arr[i], second)
        first = second
        second = temp
    
    return temp  # return second (temp & second) are in same places
    
    




# Using DP
def FindMaxSum(arr, n):
    first = 0
    second = 0
    for i in range(0, n):
        sum = first + arr[i]
        first = second
        second = max(second, sum)
    
    return second
