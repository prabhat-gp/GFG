# Trapping Rain Water

# Approach 1
def trappingWater(arr, n):
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(arr[i], left_max[i - 1])
    
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(arr[i], right_max[i + 1])

    ans = 0
    for i in range(n):
        ans += min(left_max[i], right_max[i]) - arr[i] # height[i]
    
    return ans

# T.C = O(N)
# S.C = O(N)


# Space Optimised
def trappingWater(arr, n):
    low = 0
    high = n - 1
    i = 0
    j = 0
    ans = 0

    while low <= high:
        if arr[low] <= arr[high]:
            i = max(i, arr[low])
            ans += i - arr[low]
            low += 1
        elif arr[low] > arr[high]:
            j = max(j, arr[high])
            ans += j - arr[high]
            high -= 1
    
    return ans

# T.C = O(N)
# S.C = O(1)