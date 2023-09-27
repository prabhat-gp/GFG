# Merge 2 Arrays without using any Extra Space

# Naive Approach
def mergeArrays(arr1, n1, arr2, n2):
    arr3 = [0] * (n1 + n2)

    left = 0
    right = 0
    index = 0

    while(left < n1 and right < n2):
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1

    while left < n1:
        arr3[index] = arr1[left]
        left += 1
        index += 1
        
    while right < n2:
        arr3[index] = arr2[right]
        right += 1
        index += 1
    
    for i in range(0, n1 + n2):
        if i < n1:
            arr1[i] = arr3[i]
        else:
            arr2[i - n1] = arr3[i]


# T.C = O(n1 + n2) + O(n1 + n2)      
# S.C = O(n1 + n2)
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
n1 = len(arr1)
n2 = len(arr2)
mergeArrays(arr1, n1, arr2, n2)
print(*arr1, end = " ")
print(*arr2)




# Optimal Solution 1
def mergeArrays(arr1, n1, arr2, n2):
    left = n1 - 1
    right = 0

    while left >= 0 and right < n2:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()

arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
n1 = len(arr1)
n2 = len(arr2)
mergeArrays(arr1, n1, arr2, n2)
print(*arr1, end = " ")
print(*arr2)











# Optimal Solution 2
def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def mergeArrays(arr1, n1, arr2, n2):
    m = n1 + n2
    gap = (m / 2) + (m % 2)

    while gap > 0:
        left = 0
        right = left + gap
        while right < m:
            # arr1 and arr2
            if left < n1 and right >= n1:
                swapIfGreater(arr1, arr2, left, right - n1)

            # arr2 and arr2
            elif left >= n1:
                swapIfGreater(arr1, arr2, left, right - n1)
            
            # arr1 and arr1
            else:
                swapIfGreater(arr1, arr2, left, right)
            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap / 2) + (gap % 2)

        
# T.C = log(n1 + n2)

