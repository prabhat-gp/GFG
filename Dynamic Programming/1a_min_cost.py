# Min Cost Climbing Stairs (746)

# Brute Force
def minCostClimbingStairs(cost):
    n = len(cost)
    for i in range(2, n):
        cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
    
    return min(cost[n - 1], cost[n - 2])

cost = [10, 15, 20]
print(minCostClimbingStairs(cost))


# Bottom up Tablulation
def minCostClimbingStairs1(cost):
    n = len(cost)
    if n == 0 or n == 1:
        return cost[n]
    
    dp = [0] * (n + 1)

    for i in range(n):
        if i < 2:
            dp[i] = cost[i]
        else:
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    
    return min(dp[n - 1], dp[n - 2])

cost = [10, 15, 20]
print(minCostClimbingStairs1(cost))

# T.C = O(N)
# S.C = O(N)


# DP
def minCostClimbingStairs(cost):
    n = len(cost)
    first = cost[0]
    second = cost[1]

    for i in range(2, n):
        temp = (cost[i] + min(first, second))
        first = second
        second = temp
    
    return min(first, second)

cost = [10, 15, 20]
print(minCostClimbingStairs1(cost))






