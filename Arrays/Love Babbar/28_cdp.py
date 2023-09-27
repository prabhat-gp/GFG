# Chocolate Distribution Problem
# arr = Array of n integers
# each value of n = number of chocolates in a packet
# m = students
# Each student gets exactly one packet
# Difference btw max chocos given and min chocos given is minimum


def findMinDiff(arr, n, m):
    arr.sort()

    low = 0
    high = m - 1
    mini = float("inf")
    while high < n:
        diff = arr[high] - arr[low]
        mini = min(mini, diff)
        low += 1
        high += 1
    
    return mini
