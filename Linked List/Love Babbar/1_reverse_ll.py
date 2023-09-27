class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    
    # Iterative Solution
    def reverseIterative(self, head):
        curr = head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    # Recursive Solution
    def reverseRecursive(self, head):
        if head == None or head.next == None:
            return head
        newHead = self.reverseRecursive(head.next)
        headNext = head.next
        headNext.next = head
        head.next = None
        return newHead


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
print("Given linked list:")
llist.printList()


llist.head = llist.reverseIterative(llist.head)
print("\nReversed linked list using Iterative Way")
llist.printList()

llist.head = llist.reverseRecursive(llist.head)
print("\nReversed linked list using Recursive Way")
llist.printList()


