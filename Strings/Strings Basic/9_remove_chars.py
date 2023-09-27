# Remove Common Characters and Concatenate

def concatenatedString(str1, str2):
    str3 = str1 + str2
    ans = ""

    for ch in str3:
        if ch in str1 and ch in str2:
            continue
        else:
            ans += ch
    
    if not ans:
        return "-1"
    
    return ans

str1 = "geeks"
str2 = "forgeeks"
print(concatenatedString(str1, str2))
