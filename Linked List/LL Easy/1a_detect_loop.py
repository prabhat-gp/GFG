# Detect Loop in linked list

# Using map
def detectLoop(head):
    if head is None:
        return False
    
    map = {}
    temp = head
    while temp is not None:
        if map.get(temp, False):
            return True
        map[temp] = True
        temp = temp.next
    
    return False


# Approach 2
def detectLoop(head):
    temp = head
    while temp is not None:
        if temp.data == -1:
            return True
        
        temp.data = -1
        temp = temp.next
    return False


# Approach 3
def detectLoop(head):
    if head is None:
        return False
    
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
    




# Find starting point of loop

# Using map
def detectNode(head):
    if head is None:
        return -1
    
    map = {}
    temp = head
    while temp:
        if temp in map:
            return temp.data
        map[temp] = True
        temp = temp.next

    return -1



# Approach 3
def detectNode(head):
    if head is None:
        return -1
    
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if fast is not slow:
        return -1
    
    fast = head
    while fast is not slow:
        slow = slow.next
        fast = fast.next
    
    return slow.data
    # return fast.data