# Check if Linked List is Palindrome

def getMid(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse(head):
    curr = head
    prev = None
    temp = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def isPalindrome(head):
    if head is None:
        return None
    
    mid = getMid(head)

    temp = mid.next
    mid.next = reverse(temp)

    head1 = head
    head2 = mid.next

    while head2:
        if head1.data != head2.data:
            return False
        
        head1 = head1.next
        head2 = head2.next
    
    temp = mid.next
    mid.next = reverse(temp)
    return True