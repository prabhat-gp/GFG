# Reverse first k element of queue
from collections import deque
from queue import Queue as queue

def reverseK(queue, k):
    stack = []
    for _ in range(0, k):
        val = queue.get()
        stack.append(val)
    
    while stack:
        val = stack.pop()
        queue.put(val)
    
    t = len(queue) - k
    while t > 0:
        val = queue.get()
        queue.put(val)
        t -= 1
    
    return queue


# Using Deque

def reverseK(queue, k):
    dq = deque()

    for i in range(k):
        dq.appendleft(queue.popleft())

    while dq:
        queue.append(dq.popleft())

    for i in range(len(queue) - k):
        queue.append(queue.popleft())
        


