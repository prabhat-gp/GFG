# Reverse array in groups

def reverseInGroups(arr, n, k):
    for i in range(0, n, k):
        low = i
        high = min(i + k - 1, n - 1)
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
k = 3 
print(reverseInGroups(arr, n , k))
# Output = [3, 2, 1, 6, 5, 4, 8, 7]



# Reverse Integer
