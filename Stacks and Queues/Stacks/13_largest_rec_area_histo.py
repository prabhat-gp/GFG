# Largest Rectangular Area in Histogram


def getMaxArea(arr):
    stack = []
    max_area = 0
    n = len(arr)

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            height = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = arr[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area




def nextSmallerElement(self, arr, n):
    stack = []
    ans = [-1] * n  # Initialize the answer array with -1
        
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
                
        if stack:
            ans[i] = stack[-1]  # Store the index of the next smaller element
        stack.append(i)
        
    return ans

def prevSmallerElement(self, arr, n):
    stack = []
    ans = [-1] * n  # Initialize the answer array with -1
        
    for i in range(0, n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
                
        if stack:
            ans[i] = stack[-1]  # Store the index of the previous smaller element
        stack.append(i)
        
    return ans

def getMaxArea(self, heights):
    n = len(heights)

    next = self.nextSmallerElement(heights, n)
    prev = self.prevSmallerElement(heights, n)

    area = float("-inf") 
    for i in range(0, n):
        l = heights[i]
        if next[i] == -1:
            b = n - prev[i] - 1
        else:
            b = next[i] - prev[i] - 1

        newArea = l * b
        area = max(area, newArea)
        
    return area


    
# T.C = O(N) 
# S.C = O(N)
