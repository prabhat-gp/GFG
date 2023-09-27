# Check if a string is Isogram or not

def isIsogram(str):
    s = sorted(str)
    n = len(str)
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            return False
    
    return True

str = "machine"
print(isIsogram(str))

# Approach 2
def isIsogram(str):
    map = {}

    for ch in str:
        if ch in map:
            map[ch] += 1
        else:
            map[ch] = 1
    
    for val in map.values():
        if val > 1:
            return False
    
    return True
