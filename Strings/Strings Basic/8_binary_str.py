# Binary String

def binarySubstring(str, n):
    cnt = 0
    for i in range(n):
        if str[i] == '1':
            cnt += 1
    
    return (cnt * (cnt - 1)) // 2

str = '1111'
n = len(str)
print(binarySubstring(str, n))
