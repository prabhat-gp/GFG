# Largest Element in Array

# Brute Force
def largest(arr, n):
    arr.sort()
    return arr[-1]



# Method 1
def largest(arr, n):
    maxEle = arr[0]
    for i in range(n):
        maxEle = max(arr[i], maxEle)
    
    return maxEle



# Method 2
def largest(arr, n):
    maxEle = 0
    for i in range(n):
        if arr[i] > maxEle:
            maxEle = arr[i]

    return maxEle

