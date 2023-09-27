# Remove Consecutive Characters

def removeConsecutiveCharacter(str):
    n = len(str)
    res = ""
    res += str[0]
    for i in range(n):
        if str[i] != res[-1]:
            res += str[i]
    
    return res

str = "aabb"
print(removeConsecutiveCharacter(str))
