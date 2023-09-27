# Given binary array, find maximum number of consecutive 1s in this array.

def maxConsec1s(arr, n):
    cnt = 0
    maxi = 0
    for i in range(0, n):
        if arr[i] == 1:
            cnt += 1
        else: 
            cnt = 0
        
        maxi = max(cnt, maxi)
    return maxi

arr = [1, 1, 0, 1, 1, 1]
n = len(arr)
print(maxConsec1s(arr, n))

# T.C = O(N) 
# S.C = O(1)


# Maximum Number of 1s
# Maximum Consecutive 1s
