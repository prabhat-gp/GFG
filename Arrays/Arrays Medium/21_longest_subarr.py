# Longest Sub-Array with Sum K
def longestSubarrayWithSumk(arr, n, k):
    map = {}
    sum = 0
    maxLen = 0

    for i in range(0, n):
        sum += arr[i]
        if sum == k:
            maxLen = max(maxLen, i + 1) 
        rem = sum - k

        if rem in map:
            length = i - map[rem]
            maxLen = max(maxLen, length)
        
        if sum not in map:
            map[sum] = i # Adding arr[i] and index to map
        
    return maxLen




# Largest subarray with 0 sum
def maxLen(arr, n):
    map = {}  
    sum = 0  
    maxLen = 0  
    
    map[0] = -1  
    
    for i in range(n):
        sum += arr[i]  
        
        if sum in map:  
            maxLen = max(maxLen, i - map[sum])  
        
        if sum not in map:  
            map[sum] = i
        
    return maxLen





# Zero Sum Subarrays
def findSubarray(arr, n):
    result = 0
    map = {}  
    sum = 0
    
    map[0] = 1  
    
    for i in range(1, n + 1):
        sum += arr[i - 1]  
        
        if sum in map:  
            result += map[sum]  
        
        if sum not in map: 
            map[sum] = 1
        else:
            map[sum] += 1
    
    return result



# Subarrays with sum K
def findSubArraySum(arr, n, k):
    map = {} 
    map[0] = 1
    sum = 0 
    cnt = 0 
    
    for i in range(n):
        sum += arr[i]  
        
        if sum - k in map: 
            cnt += map[sum - k]  
        
        if sum in map:  
            map[sum] += 1
        else:
            map[sum] = 1
    
    return cnt
