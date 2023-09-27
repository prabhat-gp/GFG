class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # 2 -> 3 -> X
    # 1 -> 2 -> 3 -> X
    def insertAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    

    # 1 -> 2 -> 3 -> 4 -> X
    def insertAtTail(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next    
        curr.next = newNode

    # 1 -> 2 -> 5 -> 3 -> 4 -> X
    def insertAtPos(self, data, pos):
        if pos == 0:
            self.insertAtHead(data)
            return
        newNode = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if curr is None:
                raise IndexError("Pos out of bounds")
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

    ll.insertAtHead(10)
    ll.insertAtHead(20)
    ll.display()


