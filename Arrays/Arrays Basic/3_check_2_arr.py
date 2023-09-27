# Check if two arrays are equal or not

# Brute Force
def check1(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    return arr1 == arr2


# T.C = O(NlogN)
# S.C = O(N)

# Optimal
def check2(arr1, arr2, n):
    if len(arr1) != len(arr2):
        return False
    
    map = {}

    for i in range(len(arr1)):
        if arr1[i] in map:
            map[arr1[i]] += 1
        else:
            map[arr1[i]] = 1
    

    for i in range(len(arr2)):
        if arr2[i] in map:
            val = map[arr2[i]]
            if val <= 0:
                return False
            map[arr2[i]] = val - 1
        else:
            return False
    
    for key, value in map.items():
        if value != 0:
            return False
    
    return True

arr1 = [3, 2, 1]
arr2 = [2, 3, 1]
n = len(arr1)
print(check1(arr1, arr2, n))


# T.C = O(N)
# S.C = O(N)
