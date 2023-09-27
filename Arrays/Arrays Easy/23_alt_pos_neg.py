# Alternate positive and negative numbers


def rearrange(arr, n):
    pos = []
    neg = []
        
    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
        
    i = j = k = 0
    while i < len(pos) and j < len(neg):
        arr[k] = pos[i]
        k += 1
        i += 1
            
        arr[k] = neg[j]
        k += 1
        j += 1
        
    while i < len(pos):
        arr[k] = pos[i]
        k += 1
        i += 1
        
    while j < len(neg):
        arr[k] = neg[j]
        k += 1
        j += 1

    return arr

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
n = len(arr)
print(rearrange(arr, n))

# T.C = O(N)
# S.C = O(N)