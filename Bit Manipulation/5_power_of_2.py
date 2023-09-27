# Program to find whether a given number is power of 2

# Brute Force
def isPowerofTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
     
    return True
    
# T.C = O(logN) 
# Aux Space = (1)



# Using count of set bits
def isPowerOfTwo(n):
    cnt = 0
    while n > 0:
        if n & 1 == 1:
            cnt = cnt + 1
        n = n >> 1
 
    if cnt == 1:
        return 1
    return 0

# T.C = O(logN) 
# Aux Space = (1)


# Using Algorithm
def isPowerofTwo(n):
    return (n != 0) and ((n & (n - 1)) == 0)

# T.C = O(1) 
# S.C = O(1)