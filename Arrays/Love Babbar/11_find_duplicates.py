# Find unique Element
def findUnique(arr, n):
    ans = 0

    for i in range(0, n):
        ans = ans^arr[i]

    return ans

arr = [1, 1, 2, 3, 3]
n = len(arr)
print(findUnique(arr, n))



# Unique Occurences in Array - Leetcode



# Find Duplicates in an Array
# def duplicates(self, arr, n):
#     ans = 0
#     for i in range(0, n): 
#     	ans = ans^arr[i]
    	    
#     for i in range(1, n):
#     	ans = ans^i
    	   
#     return [ans]



# Find all Duplicates in an Array - Leetcode