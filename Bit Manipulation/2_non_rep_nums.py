# Given an array in which all numbers except two are repeated once. 
# (i.e. we have 2n+2 numbers and n numbers are occurring twice and the remaining two have occurred once). 
# Find those two numbers in the most efficient way.  

# Brute Force
def singleNumber(arr, n):
    arr.sort()
    ans = []

    i = 0
    while i < n:
        if i == n - 1 or arr[i] != arr[i + 1]:
            ans.append(arr[i])
        else:
            i += 1
        i += 1
    
    if n == 1:
        ans.append(arr[n - 1])
    
    return ans

# T.C = O(NlogN) 
# S.C = O(N)


# XOR methods
def singleNumber(arr, n):
    sums = 0 
    for i in range(n):
        sums = (sums ^ arr[i])
    
    sums = (sums & -sums)

    sum1 = 0
    sum2 = 0

    for i in range(n):
        if (arr[i] & sums) > 0:
            sum1 = (sum1 ^ arr[i])
        else:
            sum2 = (sum2 ^ arr[i])
    
    return min(sum1, sum2), max(sum1, sum2)
	    



