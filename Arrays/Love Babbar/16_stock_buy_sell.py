# Stock Buy Sell to maximise Profit
# 1 Transation Allowed

def stockBuySell(arr, n):
    minSoFar = arr[0]
    maxProfit = 0

    for i in range(0, n):
        minSoFar = min(minSoFar, arr[i])
        profit = arr[i] - minSoFar
        maxProfit = max(profit, maxProfit)

    return maxProfit

arr = [3, 1, 4, 8, 7, 2, 5]
n = len(arr)
print(stockBuySell(arr, n))


def stockBuySell(arr, n):
    minSoFar = arr[0]
    maxProfit = 0

    for i in range(0, n):
        if arr[i] < minSoFar:
            minSoFar = arr[i]
        profit = arr[i] - minSoFar
        maxProfit = max(profit, maxProfit)

    return maxProfit



# Infinite Transations Allowed
def stockBuyAndSell(arr, n):
    profit = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i - 1]
    
    return profit

arr = [5, 2, 7, 3, 6, 1, 2, 4]
n = len(arr)
print(stockBuyAndSell(arr, n))




# Similar Problem
# Given an array arr[] of integers, 
# find out the maximum difference between any two elements such that larger element appears after the smaller number. 

def maxDiff(arr, n):
    max_diff = arr[1] - arr[0]

    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]

    return max_diff

arr = [1, 2, 90, 10, 110]
n = len(arr)
print(maxDiff(arr, n))


# Maximum difference of sum of elements in two rows in a matrix