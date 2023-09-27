class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortedIntersect(head1, head2):
    temp = Node(0)
    curr = temp

    while head1 is not None and head2 is not None:
        if head1.data == head2.data:
            curr.next = Node(head1.data)
            curr = curr.next

            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next
    
    temp = temp.next
    return temp
        
# T.C = O(m+n)
# S.C = O(max(m,n)))
        



# Using Recursion
def sortedIntersect(head1, head2):
    if head1 is None or head2 is None:
        return None
    if head1.data < head2.data:
        return sortedIntersect(head1.next, head2)
    if head1.data > head2.data:
        return sortedIntersect(head1, head2.next)
    temp = Node(head1.data)
    temp.next = sortedIntersect(head1.next, head2.next)
    return temp


# T.C = O(m+n)
# S.C = O(max(m,n))




# Using Hashing
def sortedIntersect(head1, head2):
    res = [0] * max(head1, head2)

    set1 = set()  
    while head1 is not None:
        set1.add(head1.data)
        head1 = head1.next

    cnt = 0
    while head2 is not None:
        if head2.data in set1:
            res[cnt] = head2.data
            cnt += 1

        head2 = head2.next
    
    return res
    
