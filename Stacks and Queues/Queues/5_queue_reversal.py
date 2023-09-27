# Reverse a Queue


# Using Stack
def reverse(queue):
    stack = []
    while not queue.empty():
        stack.append(queue.get())
    for i in range(len(stack)):
        queue.put(stack.pop())
    return queue


def reverse(queue):
    stack = []
    while not queue.empty():
        ele = queue.get()
        stack.append(ele)
            
    while stack:
        ele = stack.pop()
        queue.put(ele)
    return queue


# Using Recursion
def reverse(queue):
    if queue.empty():
        return
    front = queue.get()
    reverse(queue)
    queue.put(front)
    
def rev(queue):
    reverse(queue)
    return queue

