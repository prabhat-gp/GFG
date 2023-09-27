# Nth node from end of linked list

def getNthFromLast(head, n):
    temp = head
    cnt = 0

    while temp:
        temp = temp.next
        cnt += 1

    if n > cnt:
        return -1
    
    pos = cnt - n
    i = 0
    temp = head
    while i < pos:
        temp = temp.next
        i += 1
    
    return temp.data

# Finding middle element in a linked list

def findMid(head):
    cnt = 0
    temp = head

    while temp:
        temp = temp.next
        cnt += 1
    
    temp = head
    for i in range(cnt // 2):
        temp = temp.next
    
    return temp.data

