# Nth number made of prime digits

def nthprimedigitsnumber(n):
    count = 0
    for i in range(1, 9999):
        num = i
        flag = True
        while num:
            N = num % 10
            if N not in [2, 3, 5, 7]:
                flag = False
            num //= 10
        if flag:
            count += 1
        if count == n:
            return i
        
n = 10
print(nthprimedigitsnumber(n))


# Approach 2
def primeNum(num):
    prime = {2, 3, 5, 7}

    while num:
        if num % 10 not in prime:
            return False
        num = num // 10

    return True

def nthprime(n):
    num = 2
    cnt = 0

    while True:
        if primeNum(num):
            cnt += 1
            if cnt == n:
                return num
        num += 1

num = 4
print(nthprime(num))



