def insertionsssSort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        for j in range(i - 1, 0, -1):
            if arr[j] > temp:
                arr[j + 1] = arr[j]
            else:
                break
    
    return arr

def insertionSort(arr, n):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    
    return arr


arr = [10, 1, 7, 4, 8, 2, 11]
n = len(arr)
print(insertionSort(arr, n))

# T.C = O(N^2)    
# S.C = O(1)
# Best Case = O(N) 
# Worst Case = O(N^2)