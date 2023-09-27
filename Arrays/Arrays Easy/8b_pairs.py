# Find all pairs with a given sum

# Using map
def allPairs(arr1, arr2, n1, n2, k):
    map = {}
    temp = []

    for i in range(n1):
        map[arr1[i]] = map.get(arr1[i], 0) + 1
    
    for i in range(n2):
        if (k - arr2[i]) in map:
            temp.append((k - arr2[i], arr2[i]))
    
    temp.sort()
    return temp

# T.C = O(NlogN)
# S.C = O(N)


# 2 Pointers Approach
def allPairs(arr1, arr2, n1, n2, k):
    arr1.sort()
    arr2.sort()
    temp = []
    low = 0
    high = n2 - 1

    while low < n1 and high >= 0:
        sum = arr1[low] + arr2[high]
        if sum == k:
            temp.append((arr1[low], arr2[high]))
            low += 1
            high -= 1
        elif sum < k:
            low += 1
        else:
            high -= 1

    return temp

# T.C = O(NlogN)
# S.C = O(N)


arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8]
n1 = len(arr1)
n2 = len(arr2)
k = 9






