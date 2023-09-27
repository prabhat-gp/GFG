# Book Allocation Problem


def isPossible(arr, n, m, mid):
    studentCount = 1
    pageSum = 0

    for i in range(n):
        if pageSum + arr[i] <= mid:
            pageSum += arr[i]
        else:
            studentCount += 1
            if studentCount > m or arr[i] > mid:
                return False
            
            pageSum = arr[i]
    return True




def findPages(arr, n, m):
    if m > n:
            return -1
    low = 0
    sum = 0
    ans = -1

    for i in range(n):
        sum += arr[i]
    high = sum

    while low <= high:
        mid = low + (high - low) // 2
        if isPossible(arr, n, m, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans


# 410 Split Array Largest Sum (Leetcode)
# Aggresive Cow
# Prata and Roti
# EKO
