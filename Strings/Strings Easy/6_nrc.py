# Non Repeating Character

def nonrepeatingCharacter(str):
    map = {}
    n = len(str)
    for i in range(n):
        ch = str[i]
        if ch in map:
            map[ch] += 1
        else:
            map[ch] = 1
    
    for i in range(n):
        ch = str[i]
        if map[ch] == 1:
            return ch
    
    return "$"

# T.C = O(N)
# S.C = O(k) k is the number of unique characters in the str
