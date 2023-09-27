# Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.

def areIsomorphic(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False
    
    map = {}
    for i in range(n1):
        ch1 = str1[i]
        ch2 = str2[i]

        if ch1 in map:
            if map[ch1] != ch2:
                return False
        else:
            if ch2 in map.values():
                return False
            map[ch1] = ch2

    return True