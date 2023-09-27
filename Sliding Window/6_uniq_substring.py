# Longest K unique characters substring

def longestKSubstr(str, k):
    map = {}
    n = len(str)
    j = 0
    ans = float('-inf')
    
    if len(str) < k:
        return -1
    
    for i in range(n):
        if str[i] in map:
            map[str[i]] += 1
        else:
            map[str[i]] = 1
        
        while len(map) > k:
            if map[str[j]] == 1:
                del map[str[j]]
            else:
                map[str[j]] -= 1
            j += 1
        
        if len(map) == k:
            ans = max(ans, i - j + 1)
    
    return ans
