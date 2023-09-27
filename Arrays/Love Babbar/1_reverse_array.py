# Reverse an Array

# Brute Force
def reverseArray(arr, n):
    left = 0
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(reverseArray(arr, n))



# Recursive Way
def reverseArray(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
        
    reverseArray(arr, left + 1, right - 1)

arr = [1, 2, 3, 4, 5]
reverseArray(arr, 0, 4)
print(arr)