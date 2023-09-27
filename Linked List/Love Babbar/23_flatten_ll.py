# Flatten a Linked List

class Node:
    def __init__(self, head, bottom): # child and down are same
        self.head = head
        self.next = None
        self.bottom = bottom

def flatten(head):
    if head is None:
        return None
    temp = None
    tail = head
    while tail.next is not None:
        tail = tail.next

    curr = head
    while curr is not tail:
        if curr.bottom is not None:
            tail.next = curr.bottom
            temp = curr.bottom

            while temp.next is not None:
                temp = temp.next
            tail = temp

        curr = curr.next
    return head



    
