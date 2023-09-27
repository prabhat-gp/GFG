# Maximum Index

# Brute Force
def maxIndexDiff(arr, n):
    maxDiff = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] <= arr[j] and j - i >= maxDiff:
                maxDiff = j - i
            else:
                continue
    return maxDiff


# Optimal
def maxIndexDiff(arr, N):
    right_max = [0] * N
    max_index = N - 1
    for i in range(N - 1, -1, -1):
        if arr[max_index] < arr[i]:
            max_index = i
        right_max[i] = max_index
    
    start = 0
    k = 0
    i = 0
    while i < N:
        while i < N and arr[start] <= arr[right_max[i]]:
            i += 1
        k = max(k, right_max[i - 1] - start)
        start += 1 
    return k




# Maximum Index

# Brute Force
def maxIndexDiff(arr, n):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] <= arr[j]:
                ans = max(ans, j - i)
    return ans


def maxIndexDiff(arr, n):
    v_min = [0] * n
    v_max = [0] * n
    v_min[0] = arr[0]
    v_max[n - 1] = arr[n - 1]
    for i in range(1, n):
        v_min[i] = min(v_min[i - 1], arr[i])
        v_max[n - i - 1] = max(v_max[n - i], arr[n - i - 1])
    ans = 0
    i = 0
    j = 0
    while i < n and j < n:
        if v_min[i] <= v_max[j]:
            ans = max(ans, j - i)
            j += 1
        else:
            i += 1
    return ans