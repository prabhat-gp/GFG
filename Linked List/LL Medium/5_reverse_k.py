# Reverse a Linked List in groups of given size

# Normal Reverse
def reverseList(head):
    if head is None:
        return -1

    curr = head
    temp = None
    prev = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev




# Reverse in k groups
def solve(head, size, k):
    if not head or size < k:
        return head
    
    curr = head
    temp = None
    prev = None
    cnt = 0

    while curr and cnt < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        cnt += 1
    
    head.next = solve(curr, size - k, k)
    return prev


def reverseKGroup(head, k):
    size = 0
    temp = head

    while temp:
        size += 1
        temp = temp.next

    return solve(head, size, k)



