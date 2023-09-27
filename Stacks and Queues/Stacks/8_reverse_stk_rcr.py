# Reverse Stack using Recursion
import sys
sys.setrecursionlimit(10**6)

def insertAtBottom(stack, top):
    if not stack:
        stack.append(top)
        return 
    
    num = stack.pop()
    insertAtBottom(stack, top)
    stack.append(num)

def reverse(stack):
    if not stack:
        return
    
    top = stack.pop()
    reverse(stack)
    insertAtBottom(stack, top)


# T.C = O(N) 
# S.C = O(N)