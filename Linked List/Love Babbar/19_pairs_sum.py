# Find pairs with given sum in a DLL

def checkPairs(head, target):
    arr = []

    temp = head
    while temp is not head:
        arr.append(temp.data)
        temp = temp.next

    
    n = len(arr)
    low = 0
    high = n - 1
    pairs = []
    while low < high:
        if arr[low] + arr[high] == target:
            pairs.append((arr[low], arr[high]))
            low += 1
            high -= 1
        
        elif arr[low] + arr[high] > target:
            high -= 1
        else:
            low +=  1
    return pairs


def checkPairs(head, target):
    ans = []

    slow = head
    fast = head

    while fast.next is not None:
        fast = fast.next

    while slow != fast:
        sum = slow.data + fast.data
        if sum == target:
            ans.append((slow.data, fast.data))
        if sum > target:
            fast = fast.prev
        else:
            slow = slow.next
    return ans

# T.C = O(N)
# S.C = O(N)
# Aux Space = O(1)













# Find all pairs with a given sum
# Count pairs whose sum is equal to x