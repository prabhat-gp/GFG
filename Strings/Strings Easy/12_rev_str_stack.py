# Reverse String using Stack

def reverse(s):
    stack = []
    str = ""

    for char in s:
        stack.append(char)

    while len(stack) > 0:
        str += stack.pop()
    
    return str


# T.C = O(N)
# S.C = O(N)
