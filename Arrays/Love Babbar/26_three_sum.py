# Find if there exists a triplets that sum to a given value

# Optimal Solution
def find3Numbers(self,arr, n, x):
    arr.sort()
        
    for i in range(0, n - 2):
        firstNum = arr[i]
        j = i + 1
        k = n - 1
            
        while j < k:
            secondNum = arr[j]
            thirdNum = arr[k]
                
            sum = firstNum + secondNum + thirdNum
            if sum == x:
                return True
            elif sum < x:
                j += 1
            else:
                k -= 1
            
    return False
    
# T.C = O(N2)




# Three Sum
# Brute Force
def threeSum(arr, n):
    ans = []
    
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                temp = []
                if arr[i] + arr[j] + arr[k] == 0:
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
                if len(temp) != 0:
                    ans.append(temp)
    return ans



arr= [-1, 0, 1, 2, -1, 4]
n = len(arr)
print(threeSum(arr, n))



# Better Solution using 2 Appointer Approach
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = set()
    n = len(nums)

    for i in range(0, n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        firstNum = nums[i]
        j = i + 1
        k = n - 1

        while j < k:
            secondNum = nums[j]
            thirdNum = nums[k]
            sum = firstNum + secondNum + thirdNum

            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                triplets.add((firstNum, secondNum, thirdNum))
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return triplets

arr= [-1, 0, 1, 2, -1, 4]
n = len(arr)
print(threeSum(arr, n))



# Optimal Solution