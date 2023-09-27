# Check if strings are rotations of each other or not

def areRotations(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return False

    str3 = str1 + str1
    if str2 not in str3:
        return False
    return True

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
print(areRotations(str1, str2))