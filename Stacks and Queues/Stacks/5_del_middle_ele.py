# Delete middle element from Stack

# Iterative Approach 
def deleteMiddle(stack, size):
    if size == 0:
        return 
    elif size == 1:
        return stack.pop(size // 2)
    else:
        aux_stack = []
        middle = size // 2
        for _ in range(middle):
            aux_stack.append(stack.pop())

        stack.pop()

        while len(aux_stack) != 0:
            stack.append(aux_stack.pop())

# T.C = O(N)
# S.C = O(N)


# Using Recursion
import math
def deleteMid(self, stack, size):
    middle = math.ceil((size+1)/2)
    
    def solve(stack, middle):
        if middle == 1:
            stack.pop()
            return

        val = stack.pop()
        solve(stack, middle - 1)
        stack.append(val)
            
    solve(stack, middle)
    return stack












# Approach 2
def solve(stack, cnt, size):
    if cnt == size / 2:
        stack.pop()
        return

    num = stack.top()
    stack.pop()

    solve(stack, cnt + 1, size)

    stack.push(num)


def deleteMiddle(stack, size):
    cnt = 0
    solve(stack, cnt, size)

