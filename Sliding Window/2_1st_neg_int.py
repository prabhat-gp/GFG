# First negative integer in every window of size k (Queue Application)

# Brute Force
def printFirstNegativeInteger(arr, n, k):
    i = 0
    j = 0
    res = []

    for i in range(n - k + 1):
        found = False
        negInt = 0
        for j in range(i, i + k):
            if arr[j] < 0:
                negInt = arr[j]
                found = True
                break

        if found:
            res.append(negInt)
        else:
            res.append(0)
    
    return res

     
# Optimal (Using Queue)
import queue
def printFirstNegativeInteger(arr, n, k):
    i = 0
    j = 0
    qu = queue.Queue()
    res = []

    while j < n:
        if arr[j] < 0:
            qu.put(arr[j])
        
        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            if not qu.empty():
                res.append(qu.queue[0])
                if arr[i] < 0:
                    qu.get()
            else:
                res.append(0)
            i += 1
            j += 1
    
    return res


# Optimal 2
def printFirstNegativeInteger(arr, n, k):
    i = 0
    j = 0
    res = []
    temp = []

    while j < n:
        if arr[j] < 0:
            temp.append(arr[j])
    
        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            if len(temp) == 0:
                res.append(0)
            else:
                res.append(temp[0])
                if arr[i] < 0:
                    temp.pop(0)
            i += 1
            j += 1
    
    return res
 