# You are given two numbers A and B. The task is to count the number of bits needed to be flipped to convert A to B.

def countSetBits(n):
    cnt = 0
    while n:
        n &= (n - 1)
        cnt += 1 
    return cnt  

def countBitsFlip(a, b):
    return countSetBits(a ^ b)

# T.C = O(K) k is no of bits
# Aux Space = O(1)
