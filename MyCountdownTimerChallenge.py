print("Rules of recursion: \n" \
"Call yourself with a smaller problem\n" \
"Always have a base case to stop")

def count_up(n):
    if n > 15: return
    print(n)
    count_up(n + 1)
count_up(1)

def countdown(n):
    if n < 1:
        print("Liftoff!")
        return
    print(n)
    countdown(n-1)
countdown(5)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(123))
print(factorial(13))
print(factorial(12))

from sys import setrecursionlimit as s
s(30)
print("New recursion limit: 30")
def nobasecase(n):
    return nobasecase(n)
try:
    nobasecase(1)
except RecursionError:
    print("Recursion limit of 30 reached")