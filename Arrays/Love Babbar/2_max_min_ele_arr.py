
# Brute Force
def maxMin(arr, n):
    arr.sort()

    min = arr[0]
    max = arr[-1]
    return min, max

arr = [10, 30, 15, 5, 25, 50, 35]
n = len(arr)
print(maxMin(arr, n))

# T.C = O(logN)


# Optimal Solution u