# Formula way
def o1(n, m):
    total = n * m
    print("1 iteration: 1")

def oN(n, m):
    total = 0
    for i in range(1, n + 1):
        total += m
    print(f"n iteration: {n}")

n = int(input("Enter 'n' for n*m: "))
m = int(input("Enter 'm' for n*m: "))

o1(n, m)
oN(n, m)