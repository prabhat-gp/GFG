# Count Derangements


# Tabulation (DP)
def countDerangements(n):
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 0
    if n == 1:
        return dp[1]
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % mod
    
    return dp[n]
    

# Space Optimisation
def countDerangements(n):
    mod = 10**9 + 7

    prev2 = 0
    prev1 = 0
    if n == 1:
        return prev1
    curr = 1
    prev1 = curr
    for i in range(3, n + 1):
        curr = ((i - 1) * (prev1 + prev2)) % mod
        # Shift
        prev2 = prev1
        prev1 = curr

    return curr