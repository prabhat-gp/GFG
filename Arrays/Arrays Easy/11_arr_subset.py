# Array Subset of another array

def isSubset(arr1, arr2, n1, n2):
    if n1 < n2:
        return False
    
    map = {}  
    
    for i in range(n1):
        map[arr1[i]] = map.get(arr1[i], 0) + 1

    for i in range(n2):
        if arr2[i] in map and map[arr2[i]] > 0:
            map[arr2[i]] -= 1
        else:
            return False
    
    return True


# T.C = O(max(n1, n2))
# S.C = O(N)


arr1 = [11, 7, 1, 13, 21, 3, 7, 3]
arr2 = [11, 3, 7, 1, 7]
n1 = len(arr1)
n2 = len(arr2)
print(isSubset(arr1, arr2, n1, n2))