# Delete nodes having greater value on right

def delete(head):
    temp = head
    while temp.next:
        if temp.data < temp.next.data:
            temp.data = temp.next.data
            temp.next = temp.next.next
            temp = head
        else:
            temp = temp.next
    
    return head