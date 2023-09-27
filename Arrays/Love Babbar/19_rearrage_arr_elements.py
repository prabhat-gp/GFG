# Rearrange elements by sign

# Brute Force
def rearrange(arr, n):
    pos = [0] * (n//2)
    neg = [0] * (n//2)

    for i in range(0, n):
        if arr[i] > 0:
            pos.append(i)
        else:
            neg.append(i)

    for i in range(len(pos)):
        arr[i * 2] = pos[i]
    for i in range(len(neg)):
        arr[i * 2 + 1] = neg[i]

    return arr

arr = [3, 1, -2. -5, 2, 4]
n = len(arr)
print(rearrange(arr, n))




# Optimal
def rearrange(arr, n):
    ans = [0] * n
    pos = 0
    neg = 1
    for i in range(0, n):
        if arr[i] >= 0:
            ans[pos] = arr[i]
            pos+= 2
            
        else:
            ans[neg] = arr[i]
            neg += 2
            
    return ans


arr = [3, 1, -2. -5, 2, 4]
n = len(arr)
ans = rearrange(arr, n)

for i in range(len(ans)):
    print(ans[i], end=" ")




# Alternate Numbers
# If any of the +ve or -ve numbers are left, add them at the end w/o alternating the order
def alternateNumbers(arr, n):

    pos = []
    neg = []

    for i in range(0, n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    if len(pos) < len(neg):
        for i in range(0, len(pos)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]

        index = len(pos)
        for i in range(len(neg) - len(pos)):
            arr[index] = neg[len(pos) + i]
            index += 1
    
    else:

        for i in range(0, len(neg)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]

        index = len(neg) * 2
        for i in range(len(pos) - len(neg)):
            arr[index] = pos[len(neg) + i]
            index += 1

    return arr

arr = [1, 2, -4, -5, 3, 4]
n = len(arr)

ans = alternateNumbers(arr, n)

for i in range(len(ans)):
    print(ans[i], end=" ")

