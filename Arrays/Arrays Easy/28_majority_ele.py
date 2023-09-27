# Count More than n/k Occurences 

def countOccurence(arr, n, k):
    map = {}
    cnt = 0
    
    for i in range(n):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] += 1
    
    for key, value in map.items():
        if value > n // k:
            cnt += 1
    
    return cnt



# Majority Element (n/2) Occurences
def majorityElement(arr, n):
    map = {}
    
    for i in range(n):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] += 1
    
    for key, value in map.items():
        if value > n // 2:
            return key
    
    return -1



# Optimal (Moore's Algorithm)
def majorityElement(arr, n):
    cnt = 0

    for i in range(0, n):
        if cnt == 0:
            cnt = 1
            ele = arr[i]
        elif arr[i] == ele:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0
    for i in range(0, n):
        if arr[i] == ele:
            cnt1 += 1
            
    if cnt1 > n/2:
        return ele
    return -1

arr = [1, 1, 2, 2, 3, 1, 1, 1, 2, 2, 2, 1]
n = len(arr)
print(majorityElement(arr, n))
