# Allocate Pages of Books

def isValid(maxPages, arr, n, x):
    count = 1
    books = 0
    for i in range(n):
        books += arr[i]
        if books > maxPages:
            books = arr[i]
            count += 1
            if count > x:
                return False
    return True

def findPages(arr, n, x):
    if n < x:
        return -1

    low = max(arr)
    high = sum(arr)
    ans = float('inf')

    while low <= high:
        maxPages = low + (high - low) // 2
        if isValid(maxPages, arr, n, x):
            ans = maxPages
            high = maxPages - 1
        else:
            low = maxPages + 1

    return ans
