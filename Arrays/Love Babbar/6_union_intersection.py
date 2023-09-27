def unionArray(arr1, arr2, n1, n2):
    i = 0
    j = 0
    union = []

    while(i < n1 and j < n2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < n1:  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < n2:  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return len(union)

arr1 = [1, 2, 3, 5, 7]
arr2 = [2, 4, 6, 8, 10]
n1 = len(arr1)
n2 = len(arr2)
print(unionArray(arr1, arr2, n1, n2))