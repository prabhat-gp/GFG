# Remove Duplicates

def removeDups(str):
    s = ""
    map ={}
    n = len(str)

    for i in range(n):
        if str[i] not in map:
            s += str[i]
        map[str[i]] = map.get(str[i], 0) + 1
    
    return s

# T.C = O(N)
# S.C = O(N)


def removeDups(str):
    s = ""
    for i in str:
        if i not in s:
            s += i
    
    return s
# T.C = O(N)
# S.C = O()
