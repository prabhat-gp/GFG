# Intersection of two sorted Linked lists
# Intersection of Two Linked Lists

# Approach 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findIntersection(head1, head2):
    ptr1 = None
    ptr2 = None

    if head1 is None and head2 is None:
        return None
    elif head1 is not None and head2 is None:
        return head1  
    elif head1 is None and head2 is not None:
        return head2
    else:
        temp1 = head1
        temp2 = head2
        while temp1 and temp2:
            if temp1.data < temp2.data:
                temp1 = temp1.next
            elif temp1.data > temp2.data:
                temp2 = temp2.next
            else:
                if ptr1 is None:
                    ptr1 = ptr2 = Node(temp1.data)
                else:
                    ptr2.next = Node(temp1.data)
                    ptr2 = ptr2.next
                temp1 = temp1.next
                temp2 = temp2.next
    
    return ptr1

# T.C = O(n + m)
# S.C = O(n + m)


# Approach 2
def findIntersection(head1, head2):
    map = {}
    while head2:
        map[head2.data] = True
        head2 = head2.next

    temp = Node(0)
    ptr = temp
    while head1:
        if head1.data in map:
            ptr.next = Node(head1.data)
            ptr = ptr.next
        head1 = head1.next
    
    ptr.next = None
    return temp.next

# Cant handle the case where elements are repeated