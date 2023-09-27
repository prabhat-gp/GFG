# Valid Parenthesis

def isValid(str):
    stack = []

    for ch in str:
        if ch == '(' or ch == "[" or ch == '{':
            stack.append(ch)
        else:
            if not stack:
                return False
            elif ch == ')' and stack[-1] != '(':
                return False
            elif ch == ']' and stack[-1] != '[':
                return False
            elif ch == '}' and stack[-1] != '{':
                return False
            stack.pop()
        
    return not stack

