# Find the middle of Linked List. 


# Brute Force
# * Count the number of nodes n
# * take dummy node and traverse to Return n / 2 + 1 

class Node:
    def __init__(self, head):
        self.head = head
        self.next = next

def middleEle(head):
    cnt = 0
    temp = head

    while temp:
        temp = temp.next
        cnt += 1

    temp = head
    for i in range(cnt // 2):
        temp = temp.next
    return temp
 




# Optimal
def middleEle(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
            
    return slow.data


