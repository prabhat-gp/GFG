# Count Occurences of Anagrams

def countOccurance(str, ptr):

    map = {}
    ans = 0
    # Storing the occurrences of string p in the dictionary
    for x in ptr:
        if x in map:
            map[x] += 1
        else:
            map[x] = 1

    cnt = len(map)
    n = len(str)
    k = len(ptr)
    i = 0
    j = 0

    while j < n:
        if str[j] in map:
            map[str[j]] -= 1
            if map[str[j]] == 0:
                cnt -= 1
        
        if (j - i + 1) < k:
            j += 1
        # Window length achieved, find ans and slide the window
        elif (j - i + 1) == k:
            # Finding the ans
            if cnt == 0:
                ans += 1
            if str[i] in map:
                map[str[i]] += 1
                if map[str[i]] == 1:
                    cnt += 1

            # Slide the window
            i += 1
            j += 1
    return ans

# Example usage
str = "abcbabc"
ptr = "abc"
result = countOccurance(str, ptr)
print(result)


# Storing the occurences of pattern in map
# Reduce the letter cnt in map if letter present in string
# If letter cnt == 0, map cnt -= 1
# if map cnt == 0, that is ans
# Before sliding the window, make sure necessary changes are done to ith element in map