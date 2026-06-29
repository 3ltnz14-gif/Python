n = 12  # 1100

print("===POWER SURGE===")
print("n      =", n, "->", bin(n))
print("n - 1  =", n-1, "->", bin(n-1))
print("n&(n-1)=", n & (n - 1), "->", bin(n & (n - 1)))
print()

print("Power of 2 Check")
for x in [1, 4, 6, 16, 18, 64]:
    result = x > 0 and (x & (x - 1)) == 0
    print("  ", x, "->", bin(x), "->", result)
print()

def pow4(n):
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count % 2 == 0

print("Power of 4 Check:")
for x in [1, 4, 8, 16, 32, 64]:
    print("  ", x, "->", pow4(x))
print()

def pow8(n):
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    count = 0
    while n > 1:
        n >>= 1
        count += 1
    return count % 3 == 0

print("Power of 8 Check:")
for x in [1, 8, 16, 64, 32, 512, 4096, 8192, 16384]:
    print("  ", x, "->", pow8(x))
print()

def fast_power(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result

print("Binary Exponentiation:")
print("  6 ^ 5 =", fast_power(6, 5))
print("  2 ^ 10 =", fast_power(2, 10))
print("  3 ^ 8 =", fast_power(3, 8))