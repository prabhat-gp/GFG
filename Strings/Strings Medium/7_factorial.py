# Factorial of Large Numbers

def factorial(self, N):
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    return [fact]


# Optimal for large numbers
