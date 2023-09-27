# Implement 2 Stacks in an Array
class TwoStacks:
    def __init__(self, size=100):
        self.size = size
        self.arr = [0] * size
        self.top1 = -1
        self.top2 = size

    def isEmpty1(self):
        return self.top1 == -1

    def isEmpty2(self):
        return self.top2 == self.size

    def isFull1(self):
        return self.top1 == self.top2 - 1

    def isFull2(self):
        return self.top2 == self.top1 + 1

    def push1(self, item):
        if self.isFull1():
            return -1
        else:
            self.top1 += 1
            self.arr[self.top1] = item

    def push2(self, item):
        if self.isFull2():
            return -1
        else:
            self.top2 -= 1
            self.arr[self.top2] = item

    def pop1(self):
        if self.isEmpty1():
            return -1
        else:
            item = self.arr[self.top1]
            self.top1 -= 1
            return item

    def pop2(self):
        if self.isEmpty2():
            return -1
        else:
            item = self.arr[self.top2]
            self.top2 += 1
            return item

    def display(self):
        if self.isEmpty1():
            print("The stack is empty.")
        else:
            print("Stack 1 elements:")
            for i in range(self.top1, -1, -1):
                print(self.arr[i])

            print("Stack 2 elements:")
            for i in range(self.top2, self.size):
                print(self.arr[i])


stacks = TwoStacks(4)

stacks.push1(10)
stacks.push1(20)
stacks.push2(50)
stacks.push2(60)

stacks.display()
