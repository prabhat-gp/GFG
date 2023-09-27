# Find triplets with zero sum

# Brute Force
def findTriplets(arr, n):
    found = False

    for i in range(n - 1):
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                found = True
                break
            else:
                s.add(arr[j])
        if found:
            break

    return found

# T.C = O(N^2)
# S.C = O(N)


# Optimal
def findTriplets(arr, n):
    arr.sort()
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == 0:
                return True
            elif sum > 0:
                right -= 1
            else:
                left += 1
    return False

# T.C = O(N^2logN)
# S.C = O(1)


# Triplet Sum in Array
def findTriplets(arr, n, k):
    arr.sort()
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == k:
                return True
            elif sum > k:
                right -= 1
            else:
                left += 1
    return False


# Count triplets with sum smaller than k
def countTriplets(arr, n, k):
    cnt = 0
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < k:
                cnt += right - left
                left += 1
            else:
                right -= 1
    return cnt
