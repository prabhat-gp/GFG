# Merge k Sorted Linked Lists and return in form of Array


class Node:
    def __init__(self, head):
        self.head = head
        self.next = None

def merge(self, left, right):
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
            
            
def mergeKLists(self, arr ,k):
        
    for i in range(0, k - 1):
        temp = self.merge(arr[i], arr[i + 1])
        arr[i + 1] = temp
        
    return arr[k - 1]

# Runtime Error
        
# Optimal Solution using Priority Queue