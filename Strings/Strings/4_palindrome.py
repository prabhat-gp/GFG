# Valid Palindrome I

def isPalindrome(str):
    n = len(str)
    for i in range(n):
        if str[i] != str[n - i - 1]:
            return 0
    
    return 1


def isPalindrome(str):
    n = len(str)
    low = 0
    high = n - 1

    while low <= high:
        if not str[low].isalnum():
            low += 1
            continue
        if not str[high].isalnum():
            high -= 1
            continue
        if str[low].lower() != str[high].lower():
            return False
        else:
            low += 1
            high -= 1
    
    return True



# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def isPalindrome(str, low, high):
    while low < high:
        if str[low] != str[high]:
            return False
        low += 1
        high -= 1
    
    return True

def isValid(str):
    n = len(str)
    low = 0
    high = n - 1

    while low < high:
        if str[low] == str[high]:
            low += 1
            high -= 1
        else:
            return isPalindrome(str, low + 1, high) or isPalindrome(str, low, high - 1)
    
    return True



# Palindrome Number
def isPalindrome(x):
    if x < 0:
        return False
    
    temp = x
    reversed_num = 0

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    
    return reversed_num == x

