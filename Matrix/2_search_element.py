# Search an element in a row wise and column wise sorted matrix

def searchElement(matrix, x):

    n = len(matrix)
    m = len(matrix[0])

    i = 0
    j = m - 1

    while i < n and j >= 0:
        if matrix[i][j] == x:
            return 1
        
        if matrix[i][j] > x:
            j -= 1
        else:
            i += 1

    return 0

matrix = [[3, 30, 38],
          [36, 43, 60],
          [40, 51, 69]]
x = 30
print(searchElement(matrix, x))




# Search an element
# * int sorted from left to right
# * 1st element of each row > last element of previous row
# Optimal Solution fo Leetcode Question

def searchElement(matrix, x):

    n = len(matrix)
    m = len(matrix[0])

    if n == 0 and m == 0:
        return 0 
    
    low = 0
    high = (n * m) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if matrix[mid // m][mid % m] == x:
            return 1
        
        if matrix[mid // m][mid % m] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return 0


matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
x = 30
print(searchElement(matrix, x))

