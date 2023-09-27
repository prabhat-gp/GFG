# First and Last Occurence of an Element (Array Sorted) -> Binary Search
# Problem = Search key (mid) + (mid) -> 1st Occurence
# First and Last Occurence

def firstOccurence(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            res = mid
            high = mid - 1

        elif arr[mid] > key:
            high = mid - 1
            
        else:
            low = mid + 1
    return res

def lastOccurence(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            res = mid
            low = mid + 1

        elif arr[mid] > key:
            high = mid - 1

        else:
            low = mid + 1
    
    return res

def find(arr, n, key):
    first = firstOccurence(arr, n, key)
    last = lastOccurence(arr, n, key)

    return first, last



arr = [2, 4, 10, 10, 10, 18, 20]
n = len(arr)
key = 10
# mid = 2, 4
print(find(arr, n, key))
