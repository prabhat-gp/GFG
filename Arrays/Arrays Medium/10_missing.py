# Smallest Positive missing number

# Brute Force
def missingNumber(arr, n):
    arr.sort()
    cnt = 1
    for i in range(n):
        if arr[i] == cnt:
            cnt += 1
    
    return cnt

# Optimal
def missingNumber(arr, n):
    # Marking numbers not in the range [1, n] as n + 1 (or n + x, x > 0)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1
    
    # For numbers in the range [1, n], mark the (number - 1) index as negative
    for i in range(n):
        num = abs(arr[i])
        if num != n + 1:
            if arr[num - 1] > 0:
                arr[num - 1] *= -1
    
    # Finally, the index of the first positive number in the array will be the answer
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    return n + 1
