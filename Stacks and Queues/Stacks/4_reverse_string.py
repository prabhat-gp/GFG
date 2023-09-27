# Reverse a String using Stack

def reverse(s):
    stack = []
    str = ""

    for char in s:
        stack.append(char)

    while len(stack) > 0:
        str += stack.pop()
    
    return str

s = "Prabhat"
print(reverse(s))

# T.C = O(N)
# S.C = O(N)

'''

# Applications of Stack
* Function Calls
* Undo/Redo Operations 
* Web Browser history
* Parenthesis Checking
* Expression Evaluation

'''

