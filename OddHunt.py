a, b = 7, 7
print(" == Odd Hunt ==")
print(f"a ^ a = {a ^ a}")
print(f"a ^ 0 = {a ^ 0}")
print(f"Equal (XOR): {a ^ b} == 0")
print()

arr = [3, 5, 3, 5, 9]
result = 0
for n in arr: result ^= n
print(f"XOR of: {result}")
print()

nums = [4, 7, 4, 2, 7, 2, 9]
res = 0
for n in nums: res ^= n
print(f"Odd occurring:", res)
print()

pair = [3, 9, 3, 5, 5, 7]
xab = 0
for n in pair: xab ^= n
print(f"XOR of two odds: {xab} -> {bin(xab)}")
print()

setbit = xab & -xab
x, y = 0, 0
for n in pair:
    if n & setbit: x ^= n
    else: y ^= n
print(f"Two odd-occuring: {x} and {y}")