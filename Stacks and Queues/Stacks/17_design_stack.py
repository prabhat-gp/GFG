# Implement a Stack in which you can get a minimum element in O(1) time.
# Can't use Data Structure

# Special Stack
# Brute Force
def push(stack, ele):
    stack.append(ele)


def pop(stack):
    stack.pop()


def isFull(n, stack):
    return len(stack) == n


def isEmpty(stack):
    return not stack


def getMin(n, stack):
    return min(stack)

def getMin(n, stack):
    ans = float('inf')
    while stack:
        top = stack.pop()
        ans = min(ans, top)
    return ans

# T.C = O(1) for all, O(N) for getMin 
# S.C = O(1)


# Optimal Solution
class stack:
    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, data):
        if not self.stack:
            self.stack.append(data)
            self.mini = data
        else:
            if data < self.mini:
                val = 2 * data - self.mini
                self.stack.append(val)
                self.mini = data
            else:
                self.stack.append(data)

    def pop(self):
        if not self.stack:
            return -1
        else:
            curr = self.stack.pop()
            if curr > self.mini:
                return curr
            else:
                prevMin = self.mini
                val = 2 * self.mini - curr
                self.mini = val
                return prevMin

    def top(self):
        if not self.stack:
            return -1
        curr = self.stack[-1]
        if curr < self.mini:
            return self.mini
        else:
            return curr

    def isEmpty(self):
        return not self.stack

    def getMin(self):
        if not self.stack:
            return -1
        return self.mini

# T.C = O(1) 
# S.C = O(1)