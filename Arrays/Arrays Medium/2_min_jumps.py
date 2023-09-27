# Minimum number of jumps (Not done)

# Approach 1
def minJumps(arr, n):
    if n <= 1:
        return 0
    
    if arr[0] == 0:
        return -1
    
    low = 0
    high = 0
    jumps = 0

    while high < n - 1:
        far = 0
        for i in range(low, high + 1):
            far = max(far, arr[i])
        
        if far <= high:
            return -1
        
        low = high + 1
        high = far
        jumps += 1
    
    return jumps



def minJumps(arr, n):
    if n <= 1:
        return 0
    
    if arr[0] == 0:
        return -1  
    
    maxReach = arr[0]  
    steps = arr[0]  
    jumps = 1 
    
    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        maxReach = max(maxReach, i + arr[i])
        steps -= 1
        
        if steps == 0:
            jumps += 1
            
            if i >= maxReach:
                return -1  
            
            steps = maxReach - i
    
    return -1  


# Approach 2 (Leetcode passed not gfg)
def minJumps(arr, n):
    jumps = 0
    end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])  
        if i == end:  
            end = farthest
            jumps += 1
    return jumps





# Jump Game
def canReach(arr, n):
    maxJump = 0
    for i in range(n - 1):
        maxJump = max(maxJump, arr[i])
        if maxJump == 0:
            return 0
        maxJump  -= 1
    
    return 1
