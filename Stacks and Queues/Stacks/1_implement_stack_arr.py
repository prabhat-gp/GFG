# Implement Stack using Array
class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [None] * size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow. Cannot push item:", item)
        else:
            self.top += 1
            self.arr[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow. Cannot pop from an empty stack.")
            return None
        else:
            item = self.arr[self.top]
            self.top -= 1
            return item

    def peek(self):
        if self.is_empty():
            print("The stack is empty.")
            return None
        else:
            return self.arr[self.top]

    def display(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            for i in range(self.top, -1, -1):
                print(self.arr[i])

# Example usage:
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Original Stack")
stack.display() 

print("\nAfter Stack Operations")
stack.pop()
stack.pop()
stack.display()
            