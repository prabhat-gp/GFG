# Group Anagrams

def groupAnagrams(strs):
    map = {}
    ans = []
    n = len(strs)

    for i in range(n):
        s = sorted(strs[i])
        sorted_str = "".join(s)

        if sorted_str in map:
            map[sorted_str].append(strs[i])
        else:
            map[sorted_str] = [strs[i]]
        
    for value in map.values():
        ans.append(value)
    
    return ans


arr = ['act', 'god', 'cat', 'dog','tac']
# Output = (act, cat, tac) (god, dog) = Group Anagrams

# Find all anagrams in a string (438)