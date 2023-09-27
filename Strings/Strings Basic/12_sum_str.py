# Sum of numbers in string

def findSum(str):
    total = 0
    num = 0

    for i in range(len(str)):
        if '0' <= str[i] <= '9':
            num = num * 10 + int(str[i])
        else:
            if num != 0:
                total += num
                num = 0
    
    if num != 0:
        total += num
    
    return total

str = "1abc23"
print(findSum(str))

