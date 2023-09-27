# Given an unsorted array, return the index of peak element
# A peak element is more than both its neghbours

def peakEle(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        elif mid == 0:
            if n == 1 or arr[0] > arr[1]:
                return 0
            else:
                return 1
            
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
            else:
                return n - 2 
            
        

arr = [5, 10, 20, 15]
n = len(arr) # ans = 2 
print(peakEle(arr, n))

arr1 = [10, 20, 15, 2, 23, 90, 67]
m = len(arr1) # ans = 20, 90


def peakEle(arr, n):
    n = len(arr)
    low = 0 
    high = n - 1

    while low < high: # important
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
            
    return low
