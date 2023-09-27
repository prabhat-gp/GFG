# Detect and Remove Cycle from Linked List


# Using hashmap
def detectLoop(head):
    if head is None:
        return False
    
    visited = {}

    temp = head
    while temp is not None:
        if visited.get(temp, False):
            return True

        visited[temp] = True
        temp = temp.next

    return False



# Using Floyd Cycle Detection Algorithm
def detectLoop(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None



# Find Intersection Point or Find Starting Node of the Loop
def detectNode(head):
    meet = detectLoop(head)
    if meet is None:
        return -1
    slow = head

    while slow != meet:
        slow = slow.next
        meet = meet.next
    return slow






# Remove Cycle = 5 ways
# Detect Cycle = 3 ways