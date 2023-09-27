# Minimum Platforms

def minimumPlatform(arr, dep, n):
    arr.sort()
    dep.sort()

    i = 0
    j = 0
    cnt = 0
    maxi = 0

    while i < n:
        if arr[i] <= dep[j]:
            i += 1
            cnt += 1
            maxi = max(maxi, cnt)

        else:
            j += 1
            cnt -= 1
    return maxi

# T.C = O(N)
# S.C = O(1)
