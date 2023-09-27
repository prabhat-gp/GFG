# Check whether the Linked List is Palindrome

# Brute Force

def checkPalindrome(arr):
    n = len(arr)
    low = 0
    high = n - 1
    while low < high:
        if arr[low] != arr[high]:
            return False
        low += 1
        high -= 1
    return True


def isPalindrome(head):
    arr = []

    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next

    return checkPalindrome(arr)

# T.C = O(N)
# S.C = O(N)



# Optimal
def getMid(head):
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow

def reverse(head):
    curr = head
    prev = None
    temp = None

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def isPalindrome(head):
    if head.next is None:
        return True
    
    # Find Middle
    middle = getMid(head)

    # Reverse second half
    temp = middle.next
    middle.next = reverse(temp)

    # Compare both halves
    head1 = head
    head2 = middle.next

    while head2 is not None:
        if head1.data !=  head2.data:
            return False
        
        head1 = head1.next
        head2 = head2.next
    

    # Repeat Step 2
    temp = middle.next
    middle.next = reverse(temp)

    return True

# T.C = O(N) 
# S.C = O(1)





# Check if String / Array is Palindrome

