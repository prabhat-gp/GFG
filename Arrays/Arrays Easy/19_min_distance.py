# Minimum distance between two numbers

def minDist(arr, n, x, y):
    res = float("inf")
    ans1 = []
    ans2 = []

    for i in range(n):
        if arr[i] == x:
            ans1.append(i)
        if arr[i] == y:
            ans2.append(i)

    if not ans1 or not ans2:
        return -1
    
    for i in ans1:
        for j in ans2:
            mini = abs(j - i)
            if mini < res:
                res = mini
    
    return res

arr = [1, 2, 3, 2]
n = len(arr)
x = 1
y = 2
print()

# Optimal
def minDist(arr, n, x, y):
    ind = 0
    minDiff = float('inf')
    ptrx = -1
    ptry = -1

    while ind < n:
        if arr[ind] == x:
            ptrx = ind
        if arr[ind] == y:
            ptry = ind
        if ptrx != -1 and ptry != -1:
            minDiff = min(minDiff, abs(ptrx - ptry))
        ind += 1

    if minDiff == float("inf"):
        return -1
    else:
        return minDiff
    
