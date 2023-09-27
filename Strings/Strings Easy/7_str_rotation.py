# Check if string is rotated by two places

def isRotated(str1, str2):
    n = len(str1)
    if n == 1:
        if str1[0] == str2[0]:
            return True
        else:
            return False
    
    s1 = ""  # for storing anti-clockwise rotated string
    s2 = ""  # for storing clockwise rotated string
    
    for i in range(2, n):
        s1 += str1[i]
    
    for i in range(0, 2):
        s1 += str1[i]
    
    for i in range(n - 2, n):
        s2 += str1[i]
    
    for i in range(0, n - 2):
        s2 += str1[i]
    
    if s1 == str2 or s2 == str2:
        return True
    else:
        return False

# T.C = O(N)
# S.C = O(N)