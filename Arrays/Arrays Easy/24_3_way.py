# Three way partitioning

# def threeWayPartition(array, a, b):
#     array.sort()
#     ans = []
    
#     for num in array:
#         if num < a:
#             ans.append(num)
#         elif a < num < b:
#             ans.append(num)
#         else:
#             ans.append(num)
    
#     for i in range(len(ans)):
#         array[i] = ans[i]
    
#     return ans

# arr = [1, 2, 3, 3, 4]
# [a, b] = [1, 2]
# print(threeWayPartition(arr, a, b))


def threeWayPartition(arr, a, b):
    # Dutch National Flag algorithm
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif a <= arr[mid] <= b:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr

arr = [1, 2, 3, 3, 4]
[a, b] = [1, 2]
print(threeWayPartition(arr, a, b))
