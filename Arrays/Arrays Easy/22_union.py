# Union of Two Sorted Arrays

# Approach 1
def findUnion(arr1, arr2, n1, n2):
    s = set()
    temp = []

    for i in range(n1):
        s.add(arr1[i])
    
    for i in range(n2):
        s.add(arr2[i])
    
    for i in s:
        temp.append(i)
    
    temp.sort()
    return temp

