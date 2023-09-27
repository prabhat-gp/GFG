# Merge two sorted linked lists

# Approach 1
def sortedMerge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data <= head2.data:
        head1.next = sortedMerge(head1.next, head2)
        return head1
    else:
        head2.next = sortedMerge(head1, head2.next)
        return head2
    


# Approach 2
def solve(head1, head2):
    if head1.next is None:
        head1.next = head2
        return head1

    curr1 = head1
    next1 = curr1.next
    curr2 = head2
    next2 = curr2.next

    while next1 is not None and curr2 is not None:
        if curr2.data >= curr1.data and curr2.data <= next1.data:
            # Add nodes in between first list
            curr1.next = curr2
            next2 = curr2.next
            curr2.next = next1

            # Update pointers
            curr1 = curr2
            curr2 = next2
        else:
            curr1 = next1
            next1 = next1.next

            if next1 is None:
                curr1.next = curr2
                return head1
            
    return head1


def sortedMerge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data <= head2.data:
        return solve(head1, head2)

    else:
        return solve(head2, head1)




