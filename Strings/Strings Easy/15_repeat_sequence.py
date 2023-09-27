# Second most repeated string in a sequence

def secFrequent(arr, n):
    if n == 1:
        return arr[0]
    
    map = {}
    for i in range(n):
        map[arr[i]] = map.get(arr[i], 0) + 1
    
    a = float("-inf")
    b = float("-inf")

    for i in range(n):
        if a < map[arr[i]]:
            a = map[arr[i]]
    
    for i in range(n):
        if b < map[arr[i]] < a:
            b = map[arr[i]]
            result = i

    if b == float("-inf"):
        return ""

    return arr[result]
        
arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
n = len(arr)
print(secFrequent(arr, n))

# T.C = O()
# S.C = O()

