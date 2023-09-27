# Maximum Product Subarray

# Brute Force
def maxProduct(arr, n):
    maxi = arr[0]

    for i in range(0, n):
        for j in range(i, n):
            prod = 1
            for k in range(i , j):
                prod *= arr[k]

            maxi = max(maxi, prod)

    return maxi

arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(maxProduct(arr, n))



# Better Solution
def maxProduct(arr, n):
    maxi = arr[0]

    for i in range(0, n):
        prod = 1
        for j in range(i, n):
            prod = prod * arr[j]
            maxi = max(maxi, prod)

    return maxi


arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(maxProduct(arr, n))


# Optimal Solution
def maxProduct(arr, n):
    maxp = 1
    maxs = 1
    ans = float("-inf")

    for i in range(n):
        maxp *= arr[i]
        ans = max(ans, maxp)
        if maxp == 0:
            maxp = 1
    
    for i in range(n - 1, -1, -1):
        maxs *= arr[i]
        ans = max(ans, maxs)
        if maxs == 0:
            maxs = 1
    
    return ans


arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(maxProduct(arr, n))
