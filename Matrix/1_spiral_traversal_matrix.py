# matrix[row][column]

def spirally_traverse(matrix):

    ans = []
    
    n = len(matrix) # no of rows
    m = len(matrix[0]) # no of columns

    left = 0
    right = m - 1
    top = 0
    bottom = n - 1

    while (top <= bottom and left <= right):
        # For moving left to right
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1

        # For moving top to bottom.
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        # For moving right to left.
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        
        # For moving bottom to top.
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

    return ans

         
matrix1 = [[1, 2, 3, 4, 5, 6],
          [20, 21, 22, 23, 24, 7],
          [19, 32, 33, 34, 25, 8],
          [18, 31, 36, 35, 26, 9],
          [17, 30, 29, 28, 27, 10],
          [16, 15, 14, 13, 12, 11]]


matrix2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

print(matrix1)
print(matrix2)

# T.C = O(n * m)
# S.C = O(n * m)



# Find kth element of Spiral Matrix
# Reverse Spiral form of Matrix

