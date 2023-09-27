# Given two strings a and b, if the strings are anagrams you have to return True or else return False


def anagram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    map1 = {}
    map2 = {}

    if n1 != n2:
        return False
    
    for i in range(n1):
        map1[str1[i]] = map1.get(str1[i], 0) + 1

    for i in range(n2):
        map2[str2[i]] = map2.get(str2[i], 0) + 1

    for i in range(n2):
        ch = str2[i]

        if ch in map1:
            num1 = map1[ch]
            num2 = map2[ch]
            if num1 == num2:
                continue
            else:
                return False
        
        else:
            return False
    
    return True
