# Palindrome String

# Approach 1
def isPalindrome(str):
    n = len(str)
    for i in range(n):
        if str[i] != str[n - i - 1]:
            return 0
    
    return 1

