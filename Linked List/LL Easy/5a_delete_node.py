# Delete kth Node in Single Linked List

def delNode(head, k):
    if k == 1:
        head = head.next
    else:
        temp = head
        cnt = 1
        while cnt < k - 1:
            temp = temp.next
            cnt += 1
        curr = temp.next
        temp.next = curr.next
    
    return head
         



# Delete without head pointer
def deleteNode(curr_node):
    temp = curr_node.next
    curr = curr_node
    curr.data = temp.data
    curr.next = curr.next.next




# Delete Middle of Linked List
# Approach 1
def deleteMid(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    temp.next = slow.next
    return head



# Approach 2
def length(head):
    cnt = 1
    temp = head
    while temp:
        temp = temp.next
        cnt += 1
    
    return cnt
        
def deleteMid(head):
    if head is None or head.next is None:
        return None
   
    cnt = (length(head) - 1) // 2
    temp = head
    for i in range(1, cnt):
        temp = temp.next
    temp.next = temp.next.next
    return head