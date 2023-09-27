# Longest Sub-Array with Sum K

def lenOfLongSubarr(arr, n, k):
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


# T.C = O(N)
# S.C = O(N)
# Array can contain both positive and negative numbers



# Zero Sum Subarrays
# Longest subarray with sum divisible by K
