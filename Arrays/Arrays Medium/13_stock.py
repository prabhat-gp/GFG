# Stock buy and sell (return buy and sell days)

def stockBuySell(arr, n):
    ans = []
    start = None
    end = None
    buy = 1

    for i in range(n - 1):
        if buy:
            if arr[i] < arr[i + 1]:
                buy = 0
                start = i
        elif not buy:
            if arr[i] > arr[i + 1]:
                end = i
                ans.append([start, end])
                buy = 1
    
    if buy == 0:
        ans.append([start, n - 1])
    
    return ans


# Stock buy and sell II (returns profit)
def stockBuyAndSell(price, n):
    profit = 0
    for i in range(1, n):
        if price[i] > price[i - 1]:
            profit += price[i] - price[i - 1]
    
    return profit


