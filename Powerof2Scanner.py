def pow8(n):
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count % 3 == 0

def pow4(n):
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count % 2 == 0

def pow2(n):
    return n > 0 and (n & (n - 1)) == 0

def check(n):
    if pow8(n) == True:
        return f"{n} is a power of 8"
    if pow4(n) == True:
        return f"{n} is a power of 4"
    if pow2(n) == True:
        return f"{n} is a power of 2"
    
for n in [64, 4096, 37, 1, 512, 243, 16384, 7, 256, 4096, 81, 2, 32768, 19]:
    print(check(n) or f"{n} is not a power of 2, 4, or 8")