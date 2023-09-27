# Implement strstr

# def strstr(str, x):
#     return str.find(x)


def strstr(str, x):
    n = len(str)
    m = len(x)

    for i in range(n - m + 1):
        j = 0
        while j < m and str[i + j] == x[j]:
            j += 1
        
        if j == m:
            return i
    
    return -1

str = "GeeksForGeeks"
x = "For"
print(strstr(str, x))
