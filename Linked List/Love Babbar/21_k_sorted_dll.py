# Sort a k sorted DLL 

def sortedDll(head, k):
	curr = head
	while (curr != None):
	
		temp = curr.prev
		key = curr.data
		
		while (temp != None and key < temp.data):
		
			temp.next.data = temp.data
			temp = temp.prev
		
		if (temp == None):
			head.data = key
		else:
			temp.next.data = key
		
		curr = curr.next
	
	return head


# T.C = O(N * K) 
# S.C = O(1)



# Nearly Sorted Arrays
	
	
    