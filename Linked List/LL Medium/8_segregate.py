# Segregate even and odd nodes in a Link List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def divide(head, n):
    if head is None:
        return None
    
    even = Node(-1)
    temp1 = even
    odd = Node(-1)
    temp2 = odd

    ptr = head
    while ptr:
        if ptr.data % 2 == 0:
            temp1.next = ptr
            temp1 = ptr
        else:
            temp2.next = ptr
            temp2 = ptr
        ptr = ptr.next
    
    temp1.next = odd.next
    temp2.next = None
    head = even.next

    return head
