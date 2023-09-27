# Remove duplicate element from sorted Linked List

def removeDuplicates(head):
    if head is None:
        return -1
    
    curr = head
    while curr:
        if curr.next is not None and curr.data == curr.next.data:
            temp = curr.next.next
            curr.next = None
            curr.next = temp
        else:
            curr = curr.next
    
    return head






# Remove duplicates from an unsorted linked list
# Using set (sorted and unsorted)
def removeDuplicates(head):
    if head is None:
        return -1
    
    s = set()
    s.add(head.data)
    curr = head

    while curr.next:
        if curr.next.data in s:
            curr.next = curr.next.next
        else:
            s.add(curr.next.data)
            curr = curr.next

    return head



# Using map (sorted and unsorted)
def removeDuplicates(head):
    if head is None:
        return -1

    map = {}
    curr = head

    while curr.next:
        map[curr.data] = True

        if curr.next.data in map:
            curr.next = curr.next.next
        else:
            map[curr.next.data] = True
            curr = curr.next

    return head