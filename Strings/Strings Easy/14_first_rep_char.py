# Find first repeated character

def firstRepChar(str):
    map = {}
    n = len(str)
    ans = "0"

    for i in range(n):
        map[str[i]] = map.get(str[i], 0) + 1
        if map[str[i]] > 1:
            ans = str[i]
            break
    
    if ans == "0":
        ans = "-1"
    return ans

# T.C  = O(N)
# S.C = O(N)


# Optimal
def firstRepChar(str):
    n = len(str)
    flag = 0
    copy = ""
    s = ""

    for i in range(n):
        s = str[i]
        if s in copy:
            flag = 1
            break
        copy += s
    
    if flag == 1:
        return s
    else:
        return "-1"