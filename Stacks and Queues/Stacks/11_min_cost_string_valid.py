# Minimum Cost to make string valid (Count the Reversals)

# Algorithm


def countRev(str):
    if len(str) % 2 == 1:
        return -1
    
    stack = []
    for i in range(len(str)):
        ch = str[i]
        if ch == '{':
            stack.append(ch)
        else:
            # ch is a closing brace '}'
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)

    # At this point, the stack contains only unbalanced braces.
    # Now, we need to count the number of unbalanced opening and closing braces.
    a = 0
    b = 0
    while stack:
        if stack[-1] == '{':
            b += 1
        else:
            a += 1
        stack.pop()

    # Calculate the number of reversals needed
    ans = (a+1)/2 + (b+1)/2
    return ans