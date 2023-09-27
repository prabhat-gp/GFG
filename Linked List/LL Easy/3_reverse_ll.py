# Reverse a linked list

def reverseList(head):
    if head is None:
        return -1

    curr = head
    temp = None
    prev = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev





# Reverse a Doubly Linked List
def reverseDLL(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    curr = head
    prev = None
    while curr:
        curr.prev = curr.next
        curr.next = prev
        prev = curr
        curr = curr.prev
    
    return prev
    
