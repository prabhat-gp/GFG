# Find the longest consecutive number sequence in an array

# Better Solution
def findLongestConseqSubseq(arr, n):            
    if not arr:
        return
    arr.sort()
    ans = 1
    prev = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] == prev + 1:
            cnt += 1
        elif arr[i] != prev:
            cnt = 1
        prev = arr[i]
        ans = max(ans, cnt)

    return ans

arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 2]
n = len(arr)
print(findLongestConseqSubseq(arr, n))

# T.C =O(NlogN)



# Optimal Solution
def findLongestConseqSubseq(arr, n):  
    s = set()
    ans = 0
    for ele in arr:
        s.add(ele)
    
    for i in range(0, 1):
        if arr[i] - 1 not in s:
            j = arr[i]
            while j in s:
                j += 1
            
            ans = max(ans, j - arr[i])
    return ans
            
    
