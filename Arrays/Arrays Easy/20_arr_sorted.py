# Check if array is sorted

def arraySortedOrNot(arr, n):
    x = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            x = False
            break
    return x

arr = [10, 20, 30, 40, 50]
n = len(arr)
print(arraySortedOrNot(arr, n))
