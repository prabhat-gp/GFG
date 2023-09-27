# Merge K sorted linked lists


# Approach 2
def solve(head1, head2):
    if head1.next is None:
        head1.next = head2
        return head1

    curr1 = head1
    next1 = curr1.next
    curr2 = head2
    next2 = curr2.next

    while next1 is not None and curr2 is not None:
        if curr2.data >= curr1.data and curr2.data <= next1.data:
            # Add nodes in between first list
            curr1.next = curr2
            next2 = curr2.next
            curr2.next = next1

            # Update pointers
            curr1 = curr2
            curr2 = next2
        else:
            curr1 = next1
            next1 = next1.next

            if next1 is None:
                curr1.next = curr2
                return head1
            
    return head1


def mergeKLists(arr, k):
    if k == 1:
        return arr[0]
    
    merged = solve(arr[0], arr[1])
    for i in range(k - 1):
        merged = solve(merged, arr[i])
        
    return merged










# Working

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    
    ans = Node(-1)
    temp = ans
    
    while left and right:
        if left.data <= right.data:
            temp.next = left
            temp = left
            left = left.next
        else:
            temp.next = right
            temp = right
            right = right.next
        
    while left:
        temp.next = left
        temp = left
        left = left.next
    
    while right:
        temp.next = right
        temp = right
        right = right.next
    
    return ans.next

def mergeKLists(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    
    for i in range(len(arr) - 1):
        temp = merge(arr[i], arr[i + 1])
        arr[i + 1] = temp
    
    return arr[len(arr) - 1]
