# First Repeating Element

def firstRepeated(arr, n):
    map = {}
    ans = 0
    for i in range(n - 1, -1, -1):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            ans = i + 1

    if ans == 0:
        return -1
    else:
        return ans
    

arr = [1, 5, 3, 4, 3, 5, 6]
n = len(arr)
print(firstRepeated(arr, n))

# T.C = O(N)
# S.C = O(N)




# Non-Repeating Element
def firstNonRepeating(arr, n):
    map = {}
    ans = -1
    for i in range(n):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] += 1

    for i in range(n):
        if map[arr[i]] == 1:
            ans = arr[i]
            break

    return ans

arr = [-1, 2, -1, 3, 2]
n = len(arr)
print(firstNonRepeating(arr, n))
