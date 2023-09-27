def reverseArray(arr, left, right):
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        reverseArray(arr, left + 1, right - 1)
	

def merge(arr, low, mid, high):
    left = low
    right = mid + 1

    while left <= mid  and arr[left] < 0:
        left += 1
    
    while right <= high and arr[right] < 0:
        right += 1

    reverseArray(arr, left, mid)

    reverseArray(arr, mid + 1, right - 1)

    reverseArray(arr, left, right - 1)



def rearrange(arr, low, high):
    if  low < high:
        mid = low + (high - low) // 2
        rearrange(arr, low, mid)
        rearrange(arr, mid + 1, high)

        merge(arr, low, mid, high)



arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
rearrange(arr, 0, n - 1)

for i in range(0, n):
    print(arr[i])

