'''
Types of Linked List
* Singly Linked List
* 



'''
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next


def insertAtHead(head, data):
    temp = Node(data)
    temp.next = head
    head = temp
    return head

def insertAtTail(tail, data):
    temp = Node(data)
    tail.next = temp 
    tail = temp



if __name__ == "__main__":

    # Create the linked list
    node1 = Node(10)
    head = node1
    tail = node1

    print("Original list:")
    print_list(head)

    print("At Head List")
    head = insertAtHead(head, 20)
    head = insertAtHead(head, 30)
    print_list(head)

    print("At Tail List")
    head = insertAtTail(tail, 40)
    head = insertAtTail(tail, 50)
    print_list(head)

