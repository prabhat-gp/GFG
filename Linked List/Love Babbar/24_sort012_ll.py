# Given a linked list of 0s, 1s and 2s, sort it.

# Counting Approach 1
def sort012(head):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    temp = head
    while temp is not None:
        if temp.data == 0:
            cnt0 += 1
        elif temp.data == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    
    temp = head
    while temp is not None:
        if cnt0 != 0:
            temp.data = 0
            cnt0 -= 1
        elif cnt1 != 0:
            temp.data = 1
            cnt1 -= 1
        else:
            temp.data = 2
            cnt2 -= 1

    return head

# T.C = O(2N)
# S.C = O(1)


# Counting Approach 2
def sort012(head):
    count = [0, 0, 0]
    curr = head

    while curr is not None:
        count[curr.data] += 1
        curr = curr.next
     
    curr = head
    i = 0
    while curr is not None:
        if count[i] == 0:
            i += 1
        else:
            curr.data = i
            count[i] -= 1
            curr = curr.next
                
    return head

# T.C = O(N)
# S.C = O(1)



# Pointer Approach (Data replacement is not allowed)
class Node:
    def __init__(self, head):
        self.head = head
        self.next = None

def insertAtTail(tail, curr):
    tail.next = curr
    tail = curr

def sort012(head):
    zeroHead = Node(-1)
    zeroTail = zeroHead
    oneHead = Node(-1)
    oneTail = oneHead
    twoHead = Node(-1)
    twoTail = twoHead

    curr = head

    while curr is not None:
        value = curr.data
        if value == 0:
            insertAtTail(zeroTail, curr)
        elif value == 1:
            insertAtTail(oneTail, curr)
        elif value == 2:
            insertAtTail(twoTail, curr)

        curr = curr.next

    if oneHead.next is None:
        zeroTail.next = oneHead.next
    else:
        zeroTail.next = twoHead.next
    
    oneTail.next = twoHead.next
    twoTail.next = None

    head = zeroHead.next

    return head; 