# Given a 2D array, find the row with maximum number of 1s

# Using Binary Search
def bs(arr, low, high):
    if high >= low:
        mid = low + (high - low) // 2

        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        
        elif arr[mid] == 0:
            return bs(arr, mid + 1, high)
        
        else:
            return bs(arr, low, mid - 1)
    
    return -1


def rowWithMax1s(matrix):
    n = len(matrix)
    m = len(matrix[0])

    max_row_index = 0
    max = -1
    for i in range(0, n):
        index = bs(matrix[i], 0, m - 1)
        if index != -1 and m - index > max:
            max = m - index
            max_row_index = i
    
    return max_row_index

matrix = [[0, 1, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

print(rowWithMax1s(matrix))

# T.C = O(MlogN) 
# S.C = O(logN)




# Optimal Solution

def rowWithMax1s(matrix):
    n = len(matrix)
    m = len(matrix[0])

    max_row_index = 0
    max = bs(matrix[0], 0, m - 1)

    for i in range(1, n):
        if max != -1 and matrix[i][m - max - 1] == 1:
            index = bs(matrix[i], 0, m - max)

            if index != -1 and m - index > max:
                max = m -index
                max_row_index = i

        else:
            max = bs(matrix[i], 0, m - 1)

    return max_row_index

matrix = [[0, 1, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

print(rowWithMax1s(matrix))
