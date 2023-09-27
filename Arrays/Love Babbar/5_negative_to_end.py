# Move all the negative elements to beginning
    
# Optimal Solution
def reverseArray(arr, left, right):
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        reverseArray(arr, left + 1, right - 1)
	

def merge(arr, low, mid, high):
    left = low
    right = mid + 1

    while left <= mid  and arr[left] < 0:
        left += 1
    
    while right <= high and arr[right] < 0:
        right += 1

    reverseArray(arr, left, mid)

    reverseArray(arr, mid + 1, right - 1)

    reverseArray(arr, left, right - 1)



def rearrange(arr, low, high):
    if  low < high:
        mid = low + (high - low) // 2
        rearrange(arr, low, mid)
        rearrange(arr, mid + 1, high)

        merge(arr, low, mid, high)



arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
rearrange(arr, 0, n - 1)

for i in range(0, n):
    print(arr[i])




# T.C = O(LogN) 
# S.C = O(n1 + n2 + logN)

# Using 2 Pointer Approach
def segregateElements(arr, n):
    low = 0
    high = n - 1

    while(low < high):
            if (arr[low] < 0 and arr[high] < 0):
                low += 1
            elif (arr[low] > 0 and arr[high] > 0):
                high -= 1
            elif (arr[low] > 0 and arr[high] < 0):
                arr[low], arr[high] = arr[high], arr[low]
            else:
                high -= 1

    return arr
                
arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
print(segregateElements(arr, n))





# Move all negative elements to end

# Brute Force
def segregateElements(arr, n):
    positive = []
    negative = []

    for i in arr:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)
    positive += negative
    for i in range(len(arr)):
        arr[i] = positive[i]
    return arr
        

arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
print(segregateElements(arr, n))




# Using other Approach
def segregateElements(arr, n):
        low = []
        high = []
    
        for i in arr:
            if i >= 0:
                low.append(i)
            else:
                high.append(i)
            
        arr[:n] = low + high
    
        return arr

arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
print(segregateElements(arr, n))




