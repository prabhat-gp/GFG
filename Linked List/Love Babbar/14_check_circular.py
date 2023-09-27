# Check if Linked List is circular

# Approach 1
def isCircular(head):
    temp = head.next

    while temp is not None and temp is not head:
        temp = temp.next

    if temp is None:
        return False
    if temp is head:
        return True 
    
# T.C = O(N) 
# S.C = O(1)


# Approach 2











# Count nodes of Linked List
# Linked List length even or odd?
# Identical Linked Lists