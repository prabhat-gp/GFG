# Insert an Element at its bottom in a given stack

def solve(stack, item):
    if not stack:
        stack.append(item)
        return

    num = stack.pop()
    solve(stack, item)
    stack.append(num)


def insertAtBottom(stack, size):
    solve(stack, size)
    return stack


# Example usage:
stack = [1, 2, 3, 4]
item = 5
print("Original stack:", stack)
insertAtBottom(stack, item)
print("Stack after inserting {} at the bottom:".format(item), stack)

# T.C = O(N) 
# S.C = O(N)






# Get min at pop
def push(arr, n):
    stack = []
    aux_stack = []
    
    stack.append(arr[0])
    aux_stack.append(arr[0])
    
    for i in range(1, n):
        stack.append(arr[i])
        if stack[-1] >= aux_stack[-1]:
            aux_stack.append(aux_stack[-1])
        else:
            aux_stack.append(stack[-1])
    
    return aux_stack
        
def getMinAtPop(stack):
    while stack:
        print(stack.pop(), end=" ")
    