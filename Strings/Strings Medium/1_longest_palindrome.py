# Longest Palindrome in a String

def longestPalin(str):
    start = 0
    end = 1
    n = len(str)

    for i in range(1, n):
        # Even length palindromes
        low = i - 1
        high = i

        while low >= 0 and high < n and str[low] == str[high]:
            if high - low + 1 > end:
                start = low
                end = high - low + 1
            
            low -= 1
            high += 1

        # Odd length palindromes
        low = i - 1
        high = i + 1

        while low >= 0 and high < n and str[low] == str[high]:
            if high - low + 1 > end:
                start = low
                end = high - low + 1
            
            low -= 1
            high += 1
    
    return str[start:start + end] 


str = "aaaabbaa"
print(longestPalin(str))
output = "aabbaa"

# T.C = O(S^2)
# S.C = O(1)


# DP Approach