# The Modified String

def modified(str):
    cnt = 0
    i = 0
    while i <= len(str) - 3:
        if str[i] == str[i + 1] and str[i] == str[i + 2]:
            cnt += 1
            i += 2
        else:
            i += 1
    
    return cnt

# str = "aabbbcc"
str = "aaaaa"
print(modified(str))
