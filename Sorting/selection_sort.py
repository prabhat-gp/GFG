

# Approach 1
def selectionSort(arr, n):
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        arr[i], arr[minIndex] = arr[minIndex], arr[i]




# Approach 2
def selectionSort(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j], arr[i]

# T.C = O(N^2) 
# S.C = O(1)

# Best Case = O(N^2)
# Worst Case = O(N^2)
