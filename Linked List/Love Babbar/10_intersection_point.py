# Intersection Point of Linked Lists


# Brute Force 
# Working if len(head2) > len(head1)
def intersetPoint(head1, head2):
    while head2 is not None:
        temp = head1
        while temp is not None:
            if temp.data == head2.data:  
                return temp.data
            temp = temp.next
        head2 = head2.next

    return -1





# Most Optimal Solution
def intersectionPoint(head1, head2):
    if head1 is None or head2 is None:
        return None

    d1 = head1
    d2 = head2

    while d1 != d2:
        d1 = head2 if d1 is None else d1.next
        d2 = head1 if d2 is None else d2.next

    return d1.data if d1 is not None else -1

# T.C = O(2 * max(m, n))
# S.C = O(1)


# Rotate a Linked Lists
# Merge 2 Sorted Linked Lists
# Flattening of Linked List