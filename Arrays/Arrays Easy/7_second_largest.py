# Second Largest

def print2largest(arr, n):
    first = -1
    second = -1
    
    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] < first and arr[i] > second:
            second = arr[i]
            
    return second

arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
print(print2largest(arr, n))
