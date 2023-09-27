# Count distinct pairs with difference k

def TotalPairs(arr, k):
    arr.sort()
    ans = set()
    i = 0
    j = 1
    
    while j < len(arr):
        total = arr[j] - arr[i]
        if total == k:
            ans.add((arr[i], arr[j]))
            i += 1
            j += 1
        elif total > k and i != j:
            i += 1
        else:
            j += 1
        if i == j:
            j += 1
            
    return len(ans)



