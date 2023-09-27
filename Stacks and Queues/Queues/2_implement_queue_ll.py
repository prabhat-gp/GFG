class Node:       
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item): 
        item_node = Node(item)
        if self.head is None or self.tail is None:
            self.head = item_node
            self.tail = item_node
        else:
            self.tail.next = item_node
            self.tail = self.tail.next
            # self.tail = item_node
            
    
    def pop(self):
        if self.head is None:
            return -1
        item = self.head.data
        self.head = self.head.next
        return item 