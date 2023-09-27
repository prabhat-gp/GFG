# Count set bits in an Integer

# Brute Force
def CountSetBits(n):
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt

# T.C = O(logN) 
# Aux Space = O(1)



# Recursive Approach
def CountSetBits(n):
    if n == 0:
        return 0
    else:
        return (n & 1) + CountSetBits(n >> 1)
    
# T.C = O(logN) 
# Aux Space = O(logN)
    


# Brian Kernighan’s Algorithm
def CountSetBits(n):
    cnt = 0
    while n:
        n &= (n - 1)
        cnt += 1 
    return cnt  

# T.C = O(logN) 
# Aux Space = O(1)



# Recursive Approach
def CountSetBits(n):
    if n == 0:
        return 0
    else:
        return 1 + CountSetBits(n & (n - 1))
    
# T.C = O(logN) 
# Aux Space = O(logN)
    