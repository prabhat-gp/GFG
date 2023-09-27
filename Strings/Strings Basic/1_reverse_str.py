# Reverse String

# 2 Pointer Approach (Iterative)
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
    
# Recursive Approach
def reverse(str, i):
    temp = list(str)
    n = len(temp)
    if i == n // 2:
        return 
    
    temp[i], temp[n - i - 1] = temp[n - i - 1], temp[i]
    reverse(str, i + 1)
    ans = "".join(temp)
    return ans

str = "geeks"
i = 0
print(reverse(str, i))  