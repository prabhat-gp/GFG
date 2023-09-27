# Move all zeros to end of array

def pushZerosToEnd(arr, n):
    start = 0
    end = n - 1

    result = [0] * n

    for i in range(n):
        if arr[i] != 0:
            result[start] = arr[i]
            start += 1
        else:
            result[end] = arr[i]
            end -= 1

    for i in range(n):
        arr[i] = result[i]
    
    return arr

arr = [3, 5, 0, 0, 4]
n = len(arr)
print(pushZerosToEnd(arr, n))




# Move all negative elements to end

def segregateElements(arr, n):
    ans = []

    for i in range(n):
        if arr[i] > 0:
            ans.append(arr[i])
    
    for i in range(n):
        if arr[i] < 0:
            ans.append(arr[i])
    
    for i in range(len(ans)):
        arr[i] = ans[i]
    
    return arr

arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
print(segregateElements(arr, n))
