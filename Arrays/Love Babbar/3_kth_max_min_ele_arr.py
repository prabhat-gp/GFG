# Brute Force
def kmaxMin(arr, n, k):
    arr.sort()
    min = arr[k - 1]
    max = arr[k]
    return min, max

arr = [5, 3, 0, 2, 1, 4]
n = len(arr)
k = 3
print(kmaxMin(arr, n, k)) 

# Optimal Solution using Quick Sort