# Check if There is a Valid Partition For The Array (2369)

def validPartition(arr, n):
    if n == 1:
        return False
        
    dp = [True, False, arr[0] == arr[1] if n > 1 else False]
        
    for i in range(2, n):
        currDp = False

        if arr[i] == arr[i - 1] and dp[1]:
            currDp = True
            
        elif arr[i] == arr[i - 1] == arr[i - 2] and dp[0]:
            currDp = True
            
        elif arr[i] - arr[i - 1] == 1 and arr[i - 1] - arr[i - 2] == 1 and dp[0]:
            currDp = True
            
        dp[0], dp[1], dp[2] = dp[1], dp[2], currDp
        
    return dp[2]

