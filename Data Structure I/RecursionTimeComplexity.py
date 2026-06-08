recursions = 0
def f(n):
    global recursions
    if n <= 1:
        print(f"Recursions: {recursions}")
        recursions = 0
    recursions += 1
    f(n//2)

f(2)
f(4096)
f(128)
