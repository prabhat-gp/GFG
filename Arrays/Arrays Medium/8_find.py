# Find Missing And Repeating

def findTwoElement(arr, n):
    arr.sort()
    for i in range(n - 1):
        if arr[i] == arr[i - 1]:
            rep = arr[i]
        if arr[i + 1] - arr[i] == 2:
            mis = arr[i] + 1
        elif arr[0] != 1:
            mis = 1
        elif arr[n - 1] != n:
            mis = n
    
    return (rep, mis)


arr = [1, 3, 3]
n = len(arr)