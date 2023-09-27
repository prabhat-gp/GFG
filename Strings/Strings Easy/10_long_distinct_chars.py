# Longest Distinct characters in string (Longest substring without repeating characters)

def longestSubstrDistinctChars(str):
    n = len(str)
    if n == 0:
        return 0
    
    map = {}
    long = -1
    j = 0

    for i in range(0, n):
        while j < n and str[j] not in map:
            map[str[j]] = 1
            long = max(long, j - i + 1)
            j += 1
        map.pop(str[i])
    return long

# T.C = O(N^2)
# S.C = O(N)


def longestSubstrDistinctChars(s):
    map = [-1] * 256
    left = 0
    right = 0
    n = len(str)
    length = 0

    while right < n:
        if map[ord(str[right])] != -1:
            left = max(map[ord(str[right])] + 1, left)

        map[ord(str[right])] = right

        length = max(length, right - left + 1)
        right += 1

    return length

# T.C = O(N)
# S.C = O(N)

 
# Length of the longest substring


