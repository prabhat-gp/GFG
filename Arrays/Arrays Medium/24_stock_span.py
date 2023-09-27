# Stock span problem

def calculateSpan(price, n):
    ans = [1] * n
    stack = []
    stack.append((price[0], 1))

    for i in range(1, n):
        while stack and stack[-1][0] <= price[i]:
            ans[i] += stack[-1][1]
            stack.pop()
        stack.append((price[i], ans[i]))
    
    return ans


def calculateSpan(price, n):
    ans = []
    st = []
    st.append(0)
    ans.append(1)
    
    for i in range(1, n):
        while st and price[st[-1]] <= price[i]:
            st.pop()
        
        if not st:
            span = i + 1
        else:
            span = i - st[-1]
        
        ans.append(span)
        st.append(i)
    
    return ans
