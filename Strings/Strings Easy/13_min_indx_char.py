# Minimum indexed character

def minIndexChar(str, pat):
    s = set(pat)
    n = len(str)

    for i in range(n):
        if str[i] in s:
            return i
    
    return -1

# T.C = O(N)
# S.C = O(N)

str = "geeksforgeeks"
pat = "set"
print(minIndexChar(str, pat))

# Using Map
def minIndexChar(str, pat):
    map = {}
    a = len(str)
    b = len(pat)

    for i in range(b):
        map[pat[i]] = i

    for i in range(a):
        if str[i] in map:
            return i
    
    return -1
