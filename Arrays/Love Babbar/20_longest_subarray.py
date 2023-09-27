# Longest Subarray with Sum k (Only Positives)

# Brute Force
def longestSubarrayWithSumk(arr, n, k):
    length = 0
    for i in range(0, n): 
        sum = 0
        for j in range(i, n):
            s += arr[j]

            if sum == k:
                length = max(length, j - i + 1)
    return length

arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3
print(longestSubarrayWithSumk(arr, n, k))

# T.C = O(N2)



# Using Dictionary 
def longestSubarrayWithSumk(arr, n, k):
    dict = {}
    sum = 0
    maxLen = 0

    for i in range(0, n):
        sum += arr[i]
        if sum == k:
            maxLen = max(maxLen, i + 1) 
        rem = sum - k

        if rem in dict:
            length = i - dict[rem]
            maxLen = max(maxLen, length)
        
        if sum not in dict:
            dict[sum] = i # Adding arr[i] and index to dictionary
        
    return maxLen

arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3
print(longestSubarrayWithSumk(arr, n, k))

# T.C = O(N) 
# S.C = O(N)
# Can have both negative and positive integers in Array



# Most Optimal Solution using 2 Pointer technique Only for Zeros and Positives
def longestSubarrayWithSumk(arr, n, k):
    left = 0
    right = 0

    sum = arr[0]
    maxLen = 0
    while right < n:
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1

        right += 1
        if right < n:
            sum += arr[right]
            
        if sum == k:
            maxLen = max(maxLen, right - left + 1)

    return maxLen

arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3
print(longestSubarrayWithSumk(arr, n, k))
