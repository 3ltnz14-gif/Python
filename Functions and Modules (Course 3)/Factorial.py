def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial.__doc__)
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 2:", factorial(2))
print("The factorial of 5:", factorial(5))
print("The factorial of 10:", factorial(10))