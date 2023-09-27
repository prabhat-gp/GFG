# Wave Array

# Approach 1
def convertToWave(arr, n):
    i = 0
    while i < n - 1:
        temp = arr[i + 1]
        arr[i + 1] = arr[i]
        arr[i] = temp
        i += 2
    
    return arr

arr = [1, 2, 3, 4, 5]
# arr = [2, 4, 7, 8, 9, 10]
n = len(arr)
print(convertToWave(arr, n))


# Approach 2
def convertToWave(n, arr):
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

        