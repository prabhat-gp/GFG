# Longest Common Prefix in an Array

def longestCommonPrefix(arr, n):
    arr.sort()
    str1 = arr[0]
    str2 = arr[n - 1]
    str = ""

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            str += str1[i]
        else:
            break
    
    if len(str) != 0:
        return str
    else:
        return "-1"