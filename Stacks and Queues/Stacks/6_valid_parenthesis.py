# Parenthesis Checker (Valid or Balanced Parenthesis) 

def isPar(s):
    stack = []
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in s:
        if char in mapping:
            if not stack and stack.pop() != mapping[char]:
                return False
            else:
                stack.append(char)

    return not stack


def isValidParentheses(s):
    stack = []

    for char in s:
        if char == '(' or char == '[' or char == '{':
            # Opening parenthesis encountered, push to the stack
            stack.append(char)
        else:
            # Closing parenthesis encountered
            if not stack:
                return False  # Unmatched closing parenthesis
            if char == ')' and stack[-1] != '(':
                return False  # Mismatch with last opening parenthesis
            elif char == ']' and stack[-1] != '[':
                return False  # Mismatch with last opening parenthesis
            elif char == '}' and stack[-1] != '{':
                return False  # Mismatch with last opening parenthesis
            stack.pop()  # Matched closing parenthesis, pop the corresponding opening parenthesis

    # If the stack is empty, all parentheses are matched
    return not stack

# Example usage:
input_string = "(({{[[]]}}))"
print(isValidParentheses(input_string))  # Output: True










# Longest valid Parenthesis (Hard)
# Generate Parenthesis
# Valid Expression
# Valid Substring
# Remove invalid Parenthesis
# Maximum Nesting Depth of the Parentheses
# Redundant Parenthesis (Hard)
# Outermost Parentheses