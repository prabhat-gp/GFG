# Delete at a given position 

def deleteNode(head, key):
    curr = head
    prev = None
    while curr.data != key:
        prev = curr
        curr = curr.next
    prev.next = curr.next
    return

