# Expression contains redundant bracket or not (Redundant Brackets)

def redundantBrackets(str):
    stack = []
    for i in range(0, len(str)):
        ch = str[i]
        if ch == '(' or ch == '+' or ch == '-' or ch == '*' or ch == '/':
            stack.append(ch)
        else:
            if ch == ')':
                isRedundant = True
                while stack[-1] != '(':
                    top = stack[-1]
                    if top == '+' or top == '-' or top == '*' or top == '/':
                        isRedundant = False
                    stack.pop()

                if isRedundant is True:
                    return True
                stack.pop()
    return False