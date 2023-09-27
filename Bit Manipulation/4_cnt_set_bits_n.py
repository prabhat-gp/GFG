# You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).



def countSetBitsUtil(x):
    if x <= 0:
        return 0
    else:
        if int(x % 2) == 0:
            bit = 0
        else:
            bit = 1
        return bit + countSetBitsUtil(int(x / 2))

def countSetBits(n):
    bitCount = 0
    for i in range(1, n + 1):
        bitCount += countSetBitsUtil(i)
    
    return bitCount

# T.C = O(NlogN) 
# Aux Space = O(1)