# Anagram of a String

def remAnagrams(str1, str2):
    map = {}
    cnt = 0

    for ch2 in str2:
        map[ch2] = map.get(ch2, 0) + 1
    
    for ch1 in str1:
        if ch1 in map:
            if map[ch1] != 0:
                map[ch1] -= 1
            else:
                cnt += 1
        else:
            cnt += 1

    for val in map.values():
        cnt += val
    
    return cnt

str1 = "geeks"
str2 = "feeks"
print(remAnagrams(str1, str2))

# Approach 2
def remAnagram(str1, str2):
    arr1 = [0] * 26
    arr2 = [0] * 26
        
    for ch1 in str1:
        arr1[ord(ch1) - ord('a')] += 1
        
    for ch2 in str2:
        arr2[ord(ch2) - ord('a')] += 1
        
    count = 0
    for i in range(26):
        count += abs(arr1[i] - arr2[i])
        
    return count
    
    