# def countPairs(arr, n, target):
#     hashmap = {}
#     count = 0

#     for i in range(0, n):
#         temp = target - arr[i]
#         if (temp in hashmap):
#             count += 1
#             # return [hashmap[temp], i]
#         hashmap[arr[i]] = i

#     return count
#     # return []
 

# arr = [1, 5, 7, -1, 5]
# n = len(arr)
# target = 6
# print(countPairs(arr, n, target))

# Python program to find median of matrix
# sorted row wise

from bisect import bisect_right as upper_bound

MAX = 100;

# Function to find median in the matrix
def binaryMedian(m, r, d):
	mi = m[0][0]
	mx = 0
	for i in range(r):
		if m[i][0] < mi:
			mi = m[i][0]
		if m[i][d-1] > mx :
			mx = m[i][d-1]
	
	desired = (r * d + 1) // 2
	
	while (mi < mx):
		mid = mi + (mx - mi) // 2
		place = [0];
		
		# Find count of elements smaller than or equal to mid
		for i in range(r):
			j = upper_bound(m[i], mid)
			place[0] = place[0] + j
		if place[0] < desired:
			mi = mid + 1
		else:
			mx = mid
	print ("Median is", mi)
	return
	
# Driver code
r, d = 3, 3

m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
binaryMedian(m, r, d)
# 1, 2, 3, 3, 5, 6, 6, 9, 9



# Arrays 2, 3, 5, 6, 10, 11, 14, 21, 27 .... 
# Arrays -> Linked List -> Strings -> Stacks Queues -> Binary Tree -> Bit Manipulation

