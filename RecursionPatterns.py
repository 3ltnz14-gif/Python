#Part 1
def linear(n):
    if n == 0: return
    print(n)
    linear(n-1)
linear(5)
print("\n")

#Part 2
def tail(n):
    if n == 0: return
    print(n)
    tail(n-1)
tail(5)
print("\n")

#Part 3
def head(n):
    if n == 0:
        return
    head(n)
    print(n)

#Part 4
def incdec(n):
    if n == 0: return
    print(n)
    incdec(n-1)
    print(n)
incdec(5)
print("\n")

#Part 5
def tree(n):
    if n == 0: return
    print(n)
    tree(n-1)
    tree(n-1)
tree(3)
print("\n")