# Move last element to front of a Linked List

def moveToFront(head):
    if head == None or head.next == None:
        return head
    
    curr = head
    while curr.next.next != None:
        curr = curr.next
    temp = curr.next
    curr.next = None
    temp.next = head
    head = temp
    return head

# T.C = O(N)
# S.C = O(1)