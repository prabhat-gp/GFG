# Coin Change

# DP
def count(coins, n, sum):
    dp = [0] * (sum + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]
    
    return dp[sum]


coins = [2, 3, 5, 6]
n = len(coins)
sum = 10

# T.C = O(sum * n)
# S.C = O(sum * n)




# Number of Coins
# DP
def minCoins(coins, n, val):
    dp = [float("inf")] * (val + 1)
    dp[0] = 0

    for i in range(1, val + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    
    if dp[val] == float("inf"):
        return -1
    else:
        return dp[val]
    
# T.C = O(val * n)
# S.C = O(val)