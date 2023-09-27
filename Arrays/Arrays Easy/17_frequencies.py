# Frequencies of Limited Range Array Elements

# Using map
def frequencyCount(arr, N, P):
    map = {}
    
    for i in range(N):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
            
    for i in range(N):
        if i + 1 in map:
            arr[i] = map[i + 1]
        else:
            arr[i] = 0

    return arr

arr = [2, 3, 2, 3, 5]
n = len(arr)
p = 5
print(frequencyCount(arr, n, p))

# T.C = O(N)
# S.C = O(N)



# Optimal
def frequencyCount(arr, N, P):
    X = P + 1
    for i in range(N):
        val = arr[i] % X
        if val <= N:
            idx = val - 1
            arr[idx] += X
    
    for i in range(N):
        arr[i] = arr[i] // X