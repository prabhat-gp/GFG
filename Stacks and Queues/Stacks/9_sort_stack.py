# Sort a Stack using Recursion

def sortedInsert(stack, num):
    if not stack or (stack and stack[-1] < num):
        stack.append(num)
        return
    
    top = stack.pop()
    sortedInsert(stack, num)
    stack.append(top)



def sortStack(stack):
    if not stack:
        return
    
    num = stack.pop()
    sortStack(stack)
    sortedInsert(stack, num)