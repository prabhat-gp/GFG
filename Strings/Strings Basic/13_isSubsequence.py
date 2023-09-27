# Check for subsequence

def isSubSequence(str1, str2):
    index = 0
    cnt  = 0
    for i in range(len(str2)):
        if str1[index] == str2[i]:
            cnt += 1
            if cnt == len(str1):
                return True
            index += 1
    
    return False

str1 = "geeks"
str2 = "geeksfor"
print(isSubSequence(str1, str2))
