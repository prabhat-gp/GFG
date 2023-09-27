# Find Median in a row wise sorted matrix

# Brute Force

def medianMatrix(matrix, n, m):
    median = [0] * n * m
    index = 0
    for i in range(0, n):
        for j in range(0, m):
            median[index] = matrix[i][j]
            index += 1

    return median[(n * m) // 2]

matrix = [[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]]
# arr = 1, 2, 3, 3, 5, 6, 6, 9, 9
print(medianMatrix(matrix, 3, 3))








# * Find min and max elements of matrix
# * Min element can be found by comparing first element of each row
# * Max element can be found by comparing last element of each row
# * Perform Binary Search on a range of numbers from minimum to maximum
# * Find mid of min and max
# * Get count of numbers less than our mid. Accordingly change min or max

from bisect import bisect_right as upper_bound

MAX = 100;

def binaryMedian(matrix, n, m):
    low = matrix[0][0]
    high = 0

    for i in range(0, n):
        if matrix[i][0] < low:
            low = matrix[i][0]
        elif matrix[i][m - 1] > high:
            high = matrix[i][m - 1]
    
    checkCount = (n * m + 1) // 2

    while low < high:
        mid = low + (high - low) // 2
        count = 0

        for i in range(0, n):
            find = upper_bound(matrix[i], mid)
            count += find
        if count < checkCount:
            low = mid + 1
        else:
            high = mid

    return low

matrix = [[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]]
# arr = 1, 2, 3, 3, 5, 6, 6, 9, 9
print(binaryMedian(matrix, 3, 3))

