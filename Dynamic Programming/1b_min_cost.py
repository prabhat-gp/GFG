# Climbing Stairs (70)

# Using Tabulation
def climbStairs(n): 
    dp = [0] * (n + 1)
    for i in range(n + 1):
        if i < 2:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# T.C = O(N)
# S.C = O(N)



# DP
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    first = 1
    second = 1
    for i in range(2, n + 1):
        temp = second
        second = first + second
        first = temp
    return second

# T.C = O(N)
# S.C = O(1)



# painting fence algorithm
# Rod Cutting
# Count Derangements