# Bitonic Point

def findMaximum(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        elif mid == 0:
            if n == 1 or arr[0] > arr[1]:
                return arr[0]
            else:
                return arr[1]
            
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return arr[n - 1]
            else:
                return arr[n - 2]
            
        

arr = [1, 3, 8, 12, 4, 2]
n = len(arr)
print(findMaximum(arr, n))

