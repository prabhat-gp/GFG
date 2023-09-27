# Missing number in array

# Brute Force
def missingNumber(arr, n):
    for i in range(1, n + 1):
        flag = False
        
        for j in range(n - 1):
            if arr[j] == i:
                flag = True
                break
        
        if not flag:
            return i
    
    return -1



# Approach 2
def missingNumber1(arr, n):
    currSum = (n * (n + 1)) // 2
    
    for i in range(len(arr)):
        currSum -= arr[i]
        
    return currSum



# Approach 3
def missingNumber2(arr, n):
    xor = 0
    for i in range(len(arr)):
        xor ^= arr[i]
        xor ^= (i + 1)
    
    return xor ^ n


arr = [1, 2, 3, 5]
n = 5
print(missingNumber2(arr, n))
