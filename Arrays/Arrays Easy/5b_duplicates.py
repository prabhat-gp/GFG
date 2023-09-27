# Remove duplicate elements from sorted Array

def removeDups(arr, n):
    if n == 0:
        return 0
    
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1

# arr = [2, 2, 2, 2, 2]
arr = [1, 2, 2, 4]
n = len(arr)
print(removeDups(arr, n))




# Remove all duplicates from a given string
def removeDups(str):
    s = ""
    map ={}
    n = len(str)

    for i in range(n):
        if str[i] not in map:
            s += str[i]
        map[str[i]] = map.get(str[i], 0) + 1
    
    return s

# T.C = O(N)
# S.C = O(N)


def removeDups(str):
    s = ""
    for i in str:
        if i not in s:
            s += i
    
    return s
# T.C = O(N)
# S.C = O()
