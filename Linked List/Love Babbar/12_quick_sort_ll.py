#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def quickSort(head):
    if head is None or head.next is None:
        return head

    pivot = head
    curr = head.next
    low = None
    high = None

    while curr is not None:
        temp = curr.next

        if curr.data < pivot.data:
            curr.next = low
            low = curr
        else:
            curr.next = high
            high = curr

        curr = temp

    low = quickSort(low)
    high = quickSort(high)

    pivot.next = high

    if low is None:
        return pivot

    sorted_head = low
    while low.next is not None:
        low = low.next

    low.next = pivot
    return sorted_head