# Sort an array of 0s, 1s and 2s

# Using Counting Approach
def sort012(self,arr,n):
        
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for i in range(0, n):
            if arr[i] == 0:
                cnt0 += 1
                
            elif arr[i] == 1:
                cnt1 += 1
                
            elif arr[i] == 2:
                cnt2 += 1
        
        i = 0
        
        while (cnt0 > 0):
            arr[i] = 0
            i += 1
            cnt0 -=1
            
        while(cnt1 > 0):
            arr[i] = 1
            i += 1
            cnt1 -= 1
            
        while (cnt2 > 0):
            arr[i] = 2
            i += 1
            cnt2 -= 1



# Using Pointer Approach
def sort012(self,arr,n):
    low = 0
    mid = 0
    high = n - 1
        
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
            
        elif arr[mid] == 1:
            mid += 1
            
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


