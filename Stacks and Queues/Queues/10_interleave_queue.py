# Interleave the First Half of the Queue with Second Half

from queue import Queue

# Using Queue
def rearrange_queue(q1):
    q2 = Queue()
    n = q1.qsize()
    temp = n // 2
    
    # first push first half into new queue
    while temp:
        q2.put(q1.get())
        temp -= 1
    
    ans = []
    i = 0
    while i < n:
        if i % 2 == 0:
            ans.append(q2.get())
        else:
            ans.append(q1.get())
        i += 1
    
    return ans


# Using Stack
from queue import Queue

def rearrange_queue(q):
    stack = []  # Using list as a stack
    n = q.qsize()
    siz = n // 2
    
    # Move the first half of the queue to the stack
    while siz:
        ele = q.get()
        stack.append(ele)
        siz -= 1
    
    siz = n // 2
    # Move the second half of the queue to the end of the queue
    while siz:
        ele = q.get()
        q.put(ele)
        siz -= 1
    
    siz = n // 2
    # Move the first half of the queue back to the end
    while siz:
        ele = q.get()
        q.put(ele)
        siz -= 1
    
    siz = n // 2
    # Move the second half of the queue to the stack
    while siz:
        ele = q.get()
        stack.append(ele)
        siz -= 1
    
    ans = []
    while stack:
        ans.append(q.get())
        ans.append(stack.pop())
    
    return ans

# Implement Queue using Stack 
# Implement Stack using Queue