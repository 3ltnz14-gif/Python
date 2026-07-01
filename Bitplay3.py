#Bitplay 3
#Topics: Arithmetic Swap | XOR Swap | Left Shift | Divide Without /

a = 56
b = 12

#Part 1: Swap using addition and subtraction
print("=== Bitplay 3 ===")
print(f"Before: a = {a} b = {b}")
a = a + b
b = a - b
a = a - b
print(f"Swapped: a = {a} b = {b}")
print()

#Part 2: Swap using XOR
a, b = 56, 12
a = a ^ b
b = a ^ b
a = a ^ b
print(f"XOR swap: a = {a} b = {b}")

#Part 3: Left shift doubles the number each time
print("Left shift:")
print(f"3 << 1 = {3 << 1}")
print(f"3 << 2 = {3 << 2}")
print(f"3 << 3 = {3 << 3}")
print(f"3 << 4 = {3 << 4}")
print(f"3 << 5 = {3 << 5}")
print()

#Part 4: Divide without /
def divide(a, b):
    negative = (a < 0) ^ (b < 0)
    a = abs(a)
    b - abs(b)
    count = 0
    while a >= b: 
        a -= b
        count += 1
    if negative: count = -count
    return count

print("Divide without /:")
print(f"50 / 2 = {divide(50, 2)}")
print(f"72 / 3 = {divide(72, 3)}")
print(f"-50 / 2 = {divide(-50, 2)}")
print(f"50 / -2 = {divide(50, -2)}")