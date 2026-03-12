def cube(n):
    return n**3

def bythree(n):
    if n%3 == 0:
        return cube(n)
    else:
        return False

print(bythree(9))
print(bythree(4))