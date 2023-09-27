# Add 1 to a number represented as linked list. 

def addOne(head):
    if head == None:
        return head
    if head.next == None:
        head.data += 1
        return head
    curr = head
    ptr = head
    prev = None
    while curr.next != None :
        if curr.data != 9:
            ptr = curr
        curr = curr.next
    if curr.data == 9 and ptr != None:
        curr = ptr
        curr.data += 1
        
    
        curr.data += 1
        return head
    else:
        curr.data = 0
        prev.data += 1
        return head
