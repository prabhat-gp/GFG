# Union of Two Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def union(head1, head2):
    map = {}
    temp1 = head1
    temp2 = head2

    while temp1 and temp2:
        if temp1 is not None:
            map[temp1.data] = map.get(temp1.data, 0) + 1
            temp1 = temp1.next
        if temp2 is not None:
            map[temp2.data] = map.get(temp2.data, 0) + 1
            temp2 = temp2.next
    
    ptr = None
    ans = ptr

    for data, freq in map.items():
        curr = Node(data)
        if ptr is None:
            ptr = curr
            ans = ptr
        else:
            ptr.next = curr
            ptr = curr
    
    return ans

