# Find duplicates in an array

# Approach 1
def duplicates(arr, n):
    map = {}
    temp = []

    for i in range(n):
        if arr[i] in map and map[arr[i]] == 1: # important
            temp.append(arr[i])
    
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
        
        
    if not temp:
        temp.append(-1)
        return temp
    
    temp.sort()
    return temp


# Approach 2
def duplicates(arr, n):
    arr.sort()
    ans = []
    for i in range(1, n):
        if i == n - 1:
            if arr[i] == arr[i - 1]:
                ans.append(arr[i])
        else:
            if arr[i] == arr[i - 1] and arr[i] != arr[i + 1]:
                ans.append(arr[i])
    
    if not ans:
        return [-1]
    else:
        return ans

