# Find the sqaure root of x

def binarySearch(n):
    low = 0
    high = n
    ans = - 1

    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid

        if square == n:
            return mid
        if square < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans
       

def sqrt(x):
    return binarySearch(x)
