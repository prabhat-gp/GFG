# Implement Stack using Arrays

from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return str(maxsize - 1)
    
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return str(maxsize - 1)
    
    return [len(stack) - 1]

stack = createStack()

push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))


for i in range(len(stack)):
    print(stack[i])

print(pop(stack) + " popped from stack")
