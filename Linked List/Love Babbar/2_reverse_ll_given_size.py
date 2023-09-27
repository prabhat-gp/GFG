# Reverse a Linked List 

def kReverse(head):
    if head is None:
        return None
    
    curr = head
    prev = None
    temp = None

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    if temp is not None:
        head.next = kReverse(temp)

    return prev




# Reverse a Linked List in k groups
def kReverse(head, k):
    if head is None:
        return None
    
    curr = head
    prev = None
    temp = None
    cnt = 0

    while curr is not None and cnt < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        cnt += 1

    if temp is not None:
        head.next = kReverse(temp, k)

    return prev

# T.C = O(N) 
# S.C = O(N)
 