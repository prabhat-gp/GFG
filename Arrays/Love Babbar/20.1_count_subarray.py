# Count the numer of subarray with sum k 

# Brute Force
def countSubarray(arr, n, k):
    cnt = 0
    for i in range(0, n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j):
                sum += arr[k]
            
            if sum == k: 
                cnt += 1
    return cnt

arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
n = len(arr)
k = 3
print(countSubarray(arr, n, k))


# Better Solution
def countSubarray(arr, n, k):
    cnt = 0
    for i in range(0, n):
        for j in range(i, n):
            sum += arr[j]

            if sum == k:
                cnt += 1

    return cnt 

arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
n = len(arr)
k = 3
print(countSubarray(arr, n, k))



# Optimal Solution using Prefix Sum
from collections import defaultdict

def countSubarray(arr, n, k):
    dict = defaultdict(int)
    sum = 0
    cnt = 0
    dict[0] = 1

    for i in range(0, n):
        sum += arr[i]
        rem = sum - k
        
        cnt += dict[rem]
        
        dict[sum] += 1 
        
    return cnt


arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
n = len(arr)
k = 3
print(countSubarray(arr, n, k))



# ------------------------------------------------------------------------------------


# Count number of subarrays with xor k
# Brute Force
def countSubarray(arr, n, k):
    cnt = 0
    for i in range(0, n):
        for j in range(i, n):
            xor = 0
            for k in range(i, j):
                xor ^= arr[k]
            
            if xor == k: 
                cnt += 1
    return cnt

arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
n = len(arr)
k = 3
print(countSubarray(arr, n, k))


# Optimal Solution using Prefix Sum
from collections import defaultdict

def countSubarray(arr, n, k):
    dict = defaultdict(int)
    xor = 0
    sum = 0
    cnt = 0
    dict[xor] = 1

    for i in range(0, n):
        xor *= arr[i]
        x = xor^k
        
        cnt += dict[x]
        
        dict[xor] += 1 
        
    return cnt


arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
n = len(arr)
k = 3
print(countSubarray(arr, n, k))

