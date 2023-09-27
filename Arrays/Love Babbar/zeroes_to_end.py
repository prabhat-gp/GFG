def pushZerosToEnd(arr, n):
    j = -1

    for i in range(0, n):
        if arr[i] == 0:
            j = i
            break
    
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            i += 1

# T.C = O(N)    S.C = O(1)