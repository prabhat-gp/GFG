# Maximum Size Rectangle
# Given a binary matrix, find maximum area of rectangle formed by 1s.

# def largestArea(matrix):

#     n = len(matrix)
#     m = len(matrix[0])
#     curRow = matrix[0]
#     maxAns = maxHistogram(curRow)

#     for i in range(1, n):
#         for j in range(0, n):
#             if matrix[i][j] == 1:
#                 curRow[j] += 1

#         curAns = maxHistogram(curRow) 
#         maxAns = max(maxAns, curAns)

#     return maxAns





# Largest Area Square Submatrix (Using DP)