# Rearrange Array Alternately
# Rearrange an array with O(1) extra space

# Approach 1
def rearrange(arr, n):
    low = 0
    high = n - 1
    temp = [0] * n

    for i in range(n):
        if i % 2 == 0:
            temp[i] = arr[high]
            high -= 1
        
        if i % 2 != 0:
            temp[i] = arr[low]
            low += 1
    
    for i in range(n):
        arr[i] = temp[i]
    
    return arr

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(rearrange(arr, n))

# T.C = O(N)
# S.C = O(1)



# Using Map
def rearrange(arr, n):
    map = {}

    for i in range(n):
        map[i] = arr[i]
    
    for i in range(n):
        arr[i] = map[arr[i]]
    
    return arr
