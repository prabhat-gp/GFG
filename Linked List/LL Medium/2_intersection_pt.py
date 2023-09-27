# Intersection Point in Y Shaped Linked Lists

# Approach 1
def intersetPoint(head1, head2):
    if head1 is None or head2 is None:
        return None
    
    ptr1 = head1
    ptr2 = head2

    while ptr1 != ptr2:
        if ptr1 is None:
            ptr1 = head2
        else:
            ptr1 = ptr1.next
        
        if ptr2 is None:
            ptr2 = head1
        else:
            ptr2 = ptr2.next
    
    if ptr1 is not None:
        return ptr1.data
    
    return -1
    
