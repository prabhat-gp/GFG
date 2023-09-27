# Rotate a Linked List

# Approach 1
def rotate(head, k):
    curr = head
    for i in range(1, k):
        curr = curr.next

    temp = head
    ptr = None
    while temp:
        ptr = temp
        temp = temp.next

    ptr.next = head
    head = curr.next
    curr.next = None
    return head



# Approach 2
def rotate(head, k):
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = head
    prev = None
    while k != 0:
        prev = head
        head = head.next
        k -= 1
    prev.next = None
    return head
