# Implement Queue using array

class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        # Add an item to the end of the queue (rear)
        self.queue.append(item)
        self.rear += 1

    def dequeue(self):
        # Remove the item from the front of the queue (front)
        if not self.is_empty():
            item = self.queue[self.front]
            self.front += 1
            return item
        else:
            return -1

    def is_empty(self):
        # Check if the queue is empty
        return self.front == self.rear

    def size(self):
        # Return the size of the queue
        return self.rear - self.front

