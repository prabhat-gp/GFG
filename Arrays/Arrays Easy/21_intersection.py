# Intersection of two arrays

# Approach 1
def NumberofElementsInIntersection(arr1, arr2, n1, n2):
    s1 = set()
    s2 = set()

    for i in range(n2):
        s1.add(arr2[i])
    
    for i in range(n1):
        if arr1[i] in s1:
            s2.add(arr1[i])
    
    return len(s2)


# Approach 2
def NumberofElementsInIntersection(arr1, arr2, n1, n2):
    s = set()
    cnt = 0

    if n1 < n2:
        for i in range(n1):
            s.add(arr1[i])
        for i in range(n2):
            if arr2[i] in s:
                cnt += 1
                s.remove(arr2[i])
    
    else:
        for i in range(n2):
            s.add(arr2[i])
        for i in range(n1):
            if arr1[i] in s:
                cnt += 1
                s.remove(arr1[i])
    
    return cnt

# T.C = O(n1 + n2)
# S.C = O(min(n1, n2))
