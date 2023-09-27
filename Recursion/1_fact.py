# Factorial of Number

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

# nCr
# Pascal Triangle Approach
mod = 10**9 + 7
def nCr(n, r):
    if n < r:
        return 0
    
    pascal = []
    for i in range(n + 1):
        v = [1] * (i + 1)
        for j in range(1, i):
            v[j] = (pascal[j] + pascal[j - 1]) % mod
        pascal = v
    
    return pascal[r]


# Recursion
# nCr = (n-1)C(r-1) + (n-1)C(r)
def nCr(n, r):
    if n < r:
        return 0
    if n == 0 or n == r:
        return 1
    
    return (nCr(n - 1, r - 1) + nCr(n - 1, r)) % mod
    


# DP
mod = 10**9 + 7
def nCr(n, r):
    if n < r:
        return 0
    if n == 0 and n == r:
        return 1
    
    dp = [0] * (r + 1)
    dp[0] = 1
    for i in range(n + 1):
        for j in range(min(r, i), 0,  -1):
            dp[j] = (dp[j - 1] + dp[j]) % mod
        dp[0] = 1
        
    return dp[r]
