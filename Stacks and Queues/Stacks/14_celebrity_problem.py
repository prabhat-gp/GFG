# The Celebrity Problem

def celebrity(matrix, n):
    stack = []
    for i in range(0, n):
        stack.append(i)

    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()

        if matrix[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)

    celeb = stack.pop()
    unknown = 0
    for i in range(n):
        if matrix[celeb][i] == 0:
            unknown += 1
        
    if unknown != n:
        return -1
        
    known = 0
    for i in range(n):
        if matrix[i][celeb] == 1:
            known += 1
        
    if known != n - 1:
        return -1
        
    if unknown == n and known == n - 1:
        return celeb



# More Approaches possible
# T.C = O(N)

