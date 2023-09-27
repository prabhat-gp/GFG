# Permutations of a given string

def solve(str, ans, index):
    n = len(str)
    if index >= n:
        ans.add(str)
        return
    
    for j in range(index, n):
        temp = list(str)
        temp[index], temp[j] = temp[j], temp[index]
        newStr = "".join(temp)

        solve(newStr, ans, index + 1)
        temp[index], temp[j] = temp[j], temp[index]

def permutation(str):
    ans = set()
    index = 0
    solve(str, ans, index)
    final = list(ans)
    final.sort()
    return final



# String Permutations

def solve(index, ans, str):
    n = len(str)
    if index == n:
        ans.append(''.join(str))  # Combine characters into a string before appending
        return
        
    for i in range(index, n):
        str[index], str[i] = str[i], str[index]  # Swap characters
        solve(index + 1, ans, str)
        str[index], str[i] = str[i], str[index]  # Revert the swap
    
def permutation(str):
    ans = []
    solve(list(str), 0, ans)  # Convert the string to a list for in-place swapping
    ans.sort()  # Sort the permutations lexicographically
    return ans
