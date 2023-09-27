class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow. Cannot pop from an empty stack.")
            return None
        else:
            item = self.top.data
            self.top = self.top.next
            return item

    def peek(self):
        if self.is_empty():
            print("The stack is empty.")
            return None
        else:
            return self.top.data

    def display(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            print("Stack elements:")
            current = self.top
            while current:
                print(current.data)
                current = current.next

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Top element:", stack.peek())
stack.display()

stack.pop()
stack.pop()

print("Top element after popping:", stack.peek())
stack.display()
