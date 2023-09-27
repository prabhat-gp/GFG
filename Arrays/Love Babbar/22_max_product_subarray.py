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
    pre = 0
    suf = 0
    ans = arr[0]

    for i in range(0, n):
        if pre == 0: 
            pre = 1
        if suf == 0: 
            suf = 1
        pre *= arr[i]
        suf *= arr[n - i - 1]
        ans = max(ans, max(pre, suf))

    return ans

arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(maxProduct(arr, n))
