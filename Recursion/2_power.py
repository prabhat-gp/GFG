# Power of Numbers

mod = 10**9 + 7
def power(n, r):
    if r == 0:
        return 1
    if r == 1:
        return n
    
    ans = power(n, r // 2)
    ans = (ans * ans) % mod

    if r % 2 == 1:
        ans = (ans * n) % mod
    
    return ans

