# Subarray with given sum (1 based Indeking)

# Brute Force
def subArraySum(arr, n, k):
    low = 0
    high = 0
    currSum = 0
    while high < n:
        currSum += arr[high]
        while low < high and currSum > k:
            currSum -= arr[low]
            low += 1
    
        if currSum == k:
            return [low + 1, high + 1]
        high += 1

    return [-1]



# Approach 1
def subArraySum(arr, n, k):
    temp = []
    currSum = 0
    ptr = 0

    for i in range(n):
        currSum += arr[i]

        if currSum >= k:
            while ptr < i and currSum > k:
                currSum -= arr[ptr]
                ptr += 1

            if currSum == k:
                temp.append(ptr + 1)
                temp.append(i + 1)
                break
    if not temp:
        temp.append(-1)

    return temp
    


# Optimal Approach (Sliding Window)
def subArraySum(arr, n, k):
    low = 0
    high = 0
    currSum = arr[0]
    
    while high < n:
        if currSum == k:
            return [low + 1, high + 1]
        elif currSum < k:
            high += 1
            if high == n:
                return [-1]
            currSum += arr[high]
        elif currSum > k:
            if low < high:
                currSum -= arr[low]
                low += 1
            else:
                high += 1
                low = high
                if low < n:
                    currSum = arr[low]
    
    return [-1]


arr = [1, 2, 3, 7, 5]
n = len(arr)
k = 12
print(subArraySum(arr, n, k))




# Continous Subarray Sum
def checkSubarraySum(arr, n, k):
    map = {}
    map[0] = 0
    currSum = 0
    index = 0

    for i in range(n):
        currSum += arr[i]
        if k != 0:
            currSum = currSum % k

        if currSum not in map:
            map[currSum] = index + 1
        else:
            if map[currSum] < index:
                return True
        
        index += 1
    
    return False
