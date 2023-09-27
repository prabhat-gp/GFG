# Remove Loop

# Using map
def removeLoop(head):
    map = {}
    prev = None
    temp = head

    while temp:
        if temp in map:
            prev.next = None
            break

        map[temp] = True
        prev = temp
        temp = temp.next
        


# Appraoch 3
def reomoveLoop(head):
    if head is None:
        return -1
    
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            fast = head
            while fast is not slow:
                slow = slow.next
                fast = fast.next
            
            while slow.next is not fast:
                slow = slow.next
            
            slow.next = None
            break


# Length of Loop
def countNodesinLoop(head):
    if head is None:
        return -1
    
    slow = head
    fast = head
    cnt = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            slow = slow.next
            fast.next = 0
            while slow != 0:
                slow = slow.next
                cnt += 1
            
            return cnt
    
    return 0


def countNodesinLoop(head):
    if head is None:
        return 0
    
    slow = head
    fast = head
    loop = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop = True
            break
    
    if loop:
        cnt = 1
        slow = slow.next
        while fast is not slow:
            slow = slow.next
            cnt += 1
        
        return cnt

    return 0  
