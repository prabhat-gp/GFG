# Reverse a String

# 2 Pointer Approach
def reverse(str): 
    temp = list(str)
    n = len(temp)
    low = 0
    high = n - 1

    while low < high:
        temp[low], temp[high] = temp[high], temp[low]
        low += 1
        high -= 1

    ans = "".join(temp)
    return ans



# Using Recursion
def solve(str, low, high):
    if low < high:
        str[low], str[high] = str[high], str[low]
        solve(str, low + 1, high - 1)

def reverse(str):
    n = len(str)
    solve(str, 0, n - 1)




# Using Stack
def reverse(s):
    stack = []
    str = ""

    for char in s:
        stack.append(char)

    while stack:
        str += stack.pop()
    
    return str



# Reverse the first k characters for every 2k characters in String
def reverseK(s, k):
    str = list(s)
    n = len(str)

    for i in range(0, n, 2 * k):
        low = i
        high = min(i + k - 1, n - 1)
        while low < high:
            str[low], str[high] = str[high], str[low]
            low += 1
            high -= 1
        
    return "".join(str)
    



# Reverse Vowels of a String
def solve(s):
    n = len(str)
    low = 0
    high = n - 1
    str = list(str)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    while low <= high:
        if str[low] in vowels and str[high] in vowels:
            str[low], str[high] = str[high], str[low]
            low += 1
            high -= 1
        elif str[low] not in vowels:
            low +=1
        elif str[high] not in vowels:
            high -= 1
        else:
            low += 1
            high -= 1
    
    return "".join(str)

def reverseVowels(str):
    return solve(str)



# Reverse Only Letters

# Reverse Words in a String
