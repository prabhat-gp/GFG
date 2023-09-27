# Repeated Character

def firstRep(str):
    map = {}
    index = float("inf")
    n = len(str)

    for i in range(n):
        ch = str[i]
        if ch in map:
            index = min(index, map[ch])
        else:
            map[ch] = i
    
    if index != float("inf"):
        return str[index]

    return "#"

str = "geeksforgeeks"
print(firstRep(str))
