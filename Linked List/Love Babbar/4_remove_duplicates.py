# Remove duplicates from sorted Linked List
# Iterative Approach
def removeDuplicates(head):
    if head ==  None:
        return None
    
    curr = head
    while curr != None:
        if curr.next != None and curr.data == curr.next.data:
            temp = curr.next.next
            curr.next = None
            curr.next = temp
        else:
            curr = curr.next
    return head

# T.C = O(N)
# S.C = O(1)




# Recursive Approach
def removeDuplicates(head):
    if head == None or head.next == None:
        return head
    
    if head.data == head.next.data:
        temp = head.next.next
        head.next = None
        head.next = temp
        removeDuplicates(head)
    else:
        removeDuplicates(head.next)
    return head



# Remove duplicates from unsorted Linked List
# Brute Force
def removeDuplicates(head):
    if head == None:
        return None
    curr = head
    while curr != None:
        temp = curr
        while temp.next != None:
            if curr.data == temp.next.data:
                dup = temp.next
                temp.next = temp.next.next
                dup = None
            else:
                temp = temp.next
        curr = curr.next
    return head

# T.C = O(N^2)
# S.C = O(1)    


# Optimal Solution
def removeDuplicates(head):
    if head == None:
        return
    hash = set()
    curr = head
    hash.add(head.data)
    while curr.next is not None:
        if curr.next.data in hash:
            curr.next = curr.next.next

        else:
            hash.add(curr.next.data)
            curr = curr.next

    return head

# T.C = O(N)
# S.C = O(N)

