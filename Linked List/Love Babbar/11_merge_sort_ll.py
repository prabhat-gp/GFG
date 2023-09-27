# Merge Sort for Linked List
class Node:
    def __init__(self, head):
        self.head = head
        self.next = None


def findMid(head):
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    
    ans = Node(-1)
    temp = ans

    while left is not None and right is not None:
        if left.data < right.data:
            temp.next = left
            temp = left
            left = left.next
        else:
            temp.next = right
            temp = right
            right = right.next
        
    while left is not None:
        temp.next = left
        temp = left
        left = left.next

    while right is not None:
        temp.next = right
        temp = right
        right = right.next

    ans = ans.next
    return ans


def mergeSort(head):
    if head is None or head.next is None:
        return head
    
    mid = findMid(head)
    left = head
    right = mid.next
    mid.next = None

    left = mergeSort(left)
    right = mergeSort(right)

    result = merge(left, right)

    return result






# Merge 2 Sorted Lists