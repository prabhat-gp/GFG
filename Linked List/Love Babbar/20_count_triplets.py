# Count distinct triplets that sum up to target in Linked List

# Brute Force
def countTriplets(head, x):
    ptr1 = head
    ptr2 = None
    ptr3 = None
    cnt = 0

    while ptr1 is not None:
        ptr2 = ptr1.next
        while ptr2 is not None:
            ptr3 = ptr2.next
            while ptr3 is not None:
                if (ptr1.data + ptr2.data + ptr3.data) == x:
                    cnt += 1
                ptr3 = ptr3.next
            ptr2 = ptr2.next
        ptr1 = ptr1.next
    return cnt

# T.C = O(N^3)
# S.C = O(1)

# Optimal 1
def countTriplets(head,x):
    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.val)
        temp = temp.nxt
    
    n = len(arr)
    cnt = 0
    for i in range(0, n):
        j = i + 1
        k = n - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] == x:
                cnt += 1
                j += 1
            elif arr[i] + arr[j] + arr[k] > x:
                k -= 1
            else:
                j += 1
    return cnt

# T.C = O(N^2)
# S.C = O(1)




# Using Count Pairs, count Triplets
# Efficient Approach
def countPairs(first, second, value):
    count = 0
    while (first != None and second != None and
           first != second and second.next != first):
        
        if ((first.data + second.data) == value):
            count += 1
            first = first.next
            second = second.prev

        elif ((first.data + second.data) > value):
            second = second.prev
        else:
            first = first.next
    return count
 
def countTriplets(head, x):
    if (head == None):
        return 0
    current = head
    first = None
    last = None
    count = 0
 
    last = head
     
    while (last.next != None):
        last = last.next

    while current != None:
        first = current.next
        count, current = count + countPairs(
            first, last, x - current.data), current.next

    return count
