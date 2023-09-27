# Search a row wise and column wise sorted matrix

def search(matrix, n, m, key):
    # n rows
    # m cols

    i = 0
    j = m - 1

    while i >= 0 and i < n and j >= 0 and j < m:
        if matrix[i][j] == key:
            return 1
        elif matrix[i][j] > key:
            j -= 1
        else:
            i += 1
    
    return 0

