# Nth node from end of Linked List

def getNthfromLast(head, n):
    if head == None:
        return -1
    if n == 0:
        return -1
    curr = head
    count = 0
    while curr != None:
        count += 1
        curr = curr.next
    if count < n:
        return -1
    curr = head
    for i in range(count-n):
        curr = curr.next
    return curr.data


# T.C = O(N)
# S.C = O(1)

# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1