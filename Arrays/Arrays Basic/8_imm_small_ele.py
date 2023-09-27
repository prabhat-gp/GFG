# Immediate Smaller Element

def immediateSmaller(arr, n):
    temp = arr[0]
    for i in range(1, n):
        if arr[i] < temp:
            arr[i - 1] = arr[i]
            temp = arr[i]
        else:
            arr[i - 1] = -1
            temp = arr[i]
    arr[n - 1] = -1
    return arr

arr = [4, 2, 1, 5, 3]
# arr = [5, 6, 2, 3, 1, 7]
n = len(arr)
print(immediateSmaller(arr, n))
