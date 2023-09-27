def bubbleSort(arr, n):
    for i in range(1, n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def bubbleSort(arr, n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# T.C = O(N^2) 
# S.C = O(1)

# Best Case = O(N)
# Worst Case = O(N^2)