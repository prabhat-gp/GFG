# Left Rotate an Array by one
# Move first element to last Index
def rotateArray(arr, n):
    temp = arr[0]
    
    for i in range(1, n):
        arr[i - 1] = arr[i]
    
    arr[n-1] = temp
# Output = [2, 3, 4, 5, 1]



# Left Rotate the Array by D places
def rotateArray(arr, n, d):
    d = d % n
    
    for i in range(0, d):
        temp = arr[i]

    for i in range(d, n):
        arr[i - d] = arr[i]

    j = 0
    for i in range(n - d, n):
        arr[i] = temp[j]
        j += 1

# NOT DONE




# Rotate the Array by one position in Clockwise Direction
# Move last element to first Index
def rotateArray(arr, n):
    temp = arr[-1]
    
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = temp
    return arr

# T.C = O(N)    S.C = O(1)
# Output = [5, 1, 2, 3, 4]
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rotateArray(arr, n))



# Pointer Approach
def rotate(arr, n):
    low = 0
    high = n - 1
    while low != high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
    pass
    return arr
# T.C = O(N)    S.C = O(1)
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rotate(arr, n))
