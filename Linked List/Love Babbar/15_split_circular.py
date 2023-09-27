def splitList(head, head1, head2):
    slow = head
    fast = head
   

    if head is None:
        return 

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    if fast.next.next is head:
        fast = fast.next

    head1 = head

def splitList(head, head1, head2):
    slow = head
    fast = head.next
    temp = None

    while fast.next != head:
        fast = fast.next
        if fast.next != head:
            fast = fast.next
        slow = slow.next

    temp = slow.next
    slow.next = head
    fast.next = temp
    head1 = head
    head2 = temp 

    return head1, head2


# Linked List in Zig zag Fashion
# Sorted insert for circular Linked List
# Split Singly Linked list Alternatingly