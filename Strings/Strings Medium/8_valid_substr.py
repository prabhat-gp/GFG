# Valid Substrings

def findMaxLen(str):
    stack = [-1]
    ans = 0
    n = len(str)
    
    for i in range(n):
        top = stack[-1]
    
        if top != -1 and str[i] == ')' and str[top] == '(':
            stack.pop()
            ans = max(ans, i - stack[-1])
        else:
            stack.append(i)
        
    return ans