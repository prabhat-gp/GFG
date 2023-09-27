# Segregate 0s and 1s

# Counting Approach
def segregate0and1(arr, n):
    cnt = 0

    for i in range(0, n):
        if arr[i] == 0:
            cnt0 += 1 
        
    
    for i in range(0, cnt):
        arr[i] = 0
    
    for i in range(cnt, n):
        arr[i] = 1

    return arr

# T.C = O(2N)


# Pointer Approach
def segregate0and1(arr, n):
    left  = 0
    right = n - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        
        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1





