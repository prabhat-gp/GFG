# Uncommon characters
# Given two strings A and B consisting of lowercase english characters. 
# Find the characters that are not common in the two strings. 



def UncommonChars(A, B):
    mapA = {}
    mapB = {}
    
    for ch in A:
        mapA[ch] = 1
    
    for ch in B:
        mapB[ch] = 1
    
    ans = ""
    
    for ch in range(ord('a'), ord('z')+1):
        ch = chr(ch)
        if mapA.get(ch, 0) != mapB.get(ch, 0):
            ans += ch
    
    if not ans:
        return "-1"
    
    ans = "".join(sorted(ans))
    return ans
