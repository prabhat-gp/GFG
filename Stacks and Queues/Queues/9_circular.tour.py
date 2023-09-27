# Find the first circular tour that visits all Petrol Pumps
 
# list[][0]:Petrol
# list[][1]:Distance

def tour(list, n):
    deficit = 0
    balance = 0
    start = 0
    for i in range(n):
        balance += list[i][0]- list[i][1]
        if balance < 0:
            deficit += balance
            start = i + 1
            balance = 0
    
    if deficit + balance >= 0:
        return start
    else:
        return -1
    
import queue
def tour(gas, cost):
    q = queue.Queue()
    gasSum = 0
    costSum = 0
        
    for i in range(len(cost)):
        gasSum += gas[i]
        costSum += cost[i]
        
        if gasSum < costSum:
            return -1
        
    remain = 0
    for i in range(len(cost)):
        q.put(i)
            
        if gas[i] + remain < cost[i]:
            while not q.empty():
                q.get()
            remain = 0
        else:
            remain += gas[i] - cost[i]
        
    return q.get()

# Length of longest Substring
# IPL 