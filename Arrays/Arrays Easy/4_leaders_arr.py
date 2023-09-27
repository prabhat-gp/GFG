# Leaders in an array

def leaders(arr, n):
    temp = []
    maxVal = arr[n - 1]
    
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            temp.append(arr[i])
        elif arr[i] >= maxVal:
            temp.append(arr[i])
            maxVal = arr[i]
    
    temp.reverse()
    return temp


def leaders(arr, n):
    temp = []
    maxVal = -1
    
    for i in range(n - 1, -1, -1):
        if arr[i] >= maxVal:
            maxVal = arr[i]
            temp.insert(0, arr[i])
    
    return temp
