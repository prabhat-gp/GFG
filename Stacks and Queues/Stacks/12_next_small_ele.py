# Next Smaller Element (Help Classmates)

# Brute Force
def help_classmate(arr, n):
    if arr is None:
        return None
        
    for i in range(n):
        for j in range(i+1, n):
            if j >= n:
                arr[i] = -1
            elif arr[j] < arr[i]:
                arr[i] = arr[j]
                break
            if j == n - 1:
                arr[i] = -1
            
        if i == n - 1:
            arr[i] = -1
        
    return arr


# Optimal Solution
def nextSmallerElement(self, arr, n):
    stack = []
    ans = [0] * n
        
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
                
        if not stack:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
            
        stack.append(arr[i])
        
    return ans



# Next Greater Element
def nextLargerElement(self, arr, n):
    stack = []
    ans = [0] * n
        
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
                
        if not stack:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
            
        stack.append(arr[i])
        
    return ans





# Next Greater Element






# Love Babbar Solution
# Optimal Solution
def nextSmallerElement(arr, n):
    stack = []
    stack.append(-1)
    ans = [None] * n

    for i in range(n - 1, -1, -1):
        curr = arr[i]
        while stack[-1] >= curr:
            stack.pop()
        ans[i] = stack[-1]
        stack.append(curr)
    return ans