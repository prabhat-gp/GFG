# Element with left side smaller and right side greater

def findElement(arr, n):
    pmax = False
    maxVal = arr[0]

    for i in range(1, n - 1):
        if arr[i] >= maxVal and not pmax:
            maxVal = arr[i]
            pmax = True
        if arr[i] > arr[i + 1]:
            pmax = False

    if not pmax:
        return -1

    return maxVal

arr = [4, 2, 5, 7]
n = len(arr)
print(findElement(arr, n))
