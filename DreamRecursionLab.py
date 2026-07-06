#Part 1:
print("Part 1:\nRules of Recursion:\n\n1. Call itself with a smaller problem\n2. Always have a base case to stop\n")

#Part 2: 
print("Part 2:")
def count_up(n):
    if n > 10: return
    print(n)
    count_up(n + 1)
count_up(1)
print("\n")

#Part 3:
print("Part 3:")
def countdown(n):
    if n == 0:
        print("Liftoff!") 
        return
    print(n)
    countdown(n-1)
countdown(5)
print("\n")

#Part 4:
print("Part 4:")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(factorial(4))
print(factorial(1))
print(factorial(0))
print("\n")

#Part 5:
print("Part 5:")
from sys import setrecursionlimit as s
print("Recursion limit: 1000")
s(30)
print("New recursion limit after set: 30")
def nobasecase(n):
    return nobasecase(n)
try:
    nobasecase(1)
except RecursionError:
    print("The recursion limit was reached!")