# Peak Index in Mountain Array

def peakElement(arr, n):
    low = 0 
    high = n - 1

    while low < high: # important
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
        
    return low

# T.C = O(logN) 
# Aux Space = O(1)
