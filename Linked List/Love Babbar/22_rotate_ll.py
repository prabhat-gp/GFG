# Rotate a Linked List by k places to the right


# Optimal Solution
def rotateLL(head, k):
    if head is None or head.next is None or k == 0:
        return head
    
    curr = head
    len = 1
    while curr.next is not None:
        curr = curr.next
        len += 1
    
    curr.next = head
    k = k % len
    for i in range(0, k):
        curr = curr.next
    head = curr.next
    curr.next = None
    return head


# T.C  = O(N)
# S.C = O(1)

# Rotate a doubly Linked List by N nodes




# Can we reverse the Linked List in less than O(N)?
# Why Quick Sort is preferred for Arrays and Merge Sort for Linked Lists ?
'''
Quick Sort is preferred for Arrays
* Quick sort doesn't require any space while merge sort requires space. S.C = O(N) for merge sort
* Fast and efficient for arrays, especially for large datasets.
* Good cache locality which minimizes the number of cache misses.

Merge Sort is preferred for Linked Lists
* Suitable for sorting large datasets and linked lists.
* Guaranteed worst-case time complexity of O(n*log(n)).
* The main difference is memory allocations of arrays and linked lists

Quick Sort
* Worst Case = O(N^2)

Merge Sort
* Worst and Average Case = O(NlogN)

'''