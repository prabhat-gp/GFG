# Convert array into Zig-Zag fashion

def zigZag(arr, n):
    flag = True
    temp = 0

    for i in range(n - 1):
        if flag:
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        else:
            if arr[i] < arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        
        flag = not flag
    
    return arr

arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
print(zigZag(arr, n))
# 3 < 7 > 4 < 8 > 2 < 6 > 1
