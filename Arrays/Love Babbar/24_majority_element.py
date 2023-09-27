# Given an array of integers, find the element that appears more than n/2 times

def majorityElement(arr, n):
    for i in range(0, n):
        cnt = 0
        for j in range(0, n):
            if arr[j] == arr[i]:
                cnt += 1

        if cnt > n/2:
            return arr[i]

arr = [3,1,2,2,1,2,3,3, 3, 3, 3, 3]
n = len(arr)
print(majorityElement(arr, n))

# If there is a count and we have to track of how many times it occurs the only technique that comes to mind is hashing


# Better Solution
def majorityElement(arr, n):
    dict = {}
    for i in range(0, n):
        dict[arr[i]] += 1
    
    for i in dict:
        if dict[i] > n / 2:
            return dict[i]

arr = [1, 1, 2, 2, 3, 1, 1, 1, 2, 2, 2, 1]
n = len(arr)
print(majorityElement(arr, n))

 

# Using Moore's Algorithm
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



