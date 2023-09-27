# Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertAtTail(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode = self.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            newNode.next = curr.next
            curr.next = newNode

    def insertAtPos(self, data, pos):
        if pos == 0:
            self.insertAtHead(data)
            return
        newNode = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if curr is None:
                raise IndexError
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()

    ll.insertAtTail(10)
    ll.insertAtHead(30)
    ll.insertAtPos(20, 2)
    ll.insertAtHead(40)

   

    ll.display()




