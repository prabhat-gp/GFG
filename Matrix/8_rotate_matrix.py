# Rotate Matrix by 90 degrees

# Brute Force 
# Create auxiliary matrix and put elements in that matrix





# Optimal Solution
# * Transpose the matrix
# * Revese each row

def rotateMatrix(matrix):
    n = len(matrix)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(0, n):
        matrix[i].reverse()

    return matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(rotateMatrix(matrix))
