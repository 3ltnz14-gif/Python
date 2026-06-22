#BIT EXPLORER
#Topics: Bits & Binary, and/or, not/xor, shifts, odd/even, count bits

a = 10 #binary = 1010
b = 6 #binary = 0110

def bits(n, width = 4):
    return format(n & ((1 << width) - 1), f'0{width}b')
#Part 1: Bits & Binary
print("=== Bit explorer ===")
print("a =", a, "->", bits(a))
print("b =", b, "->", bits(b))
print()

#Part 2: And & Or
print("AND a & b =", a & b, "->", bits(a & b))
#Both 1 = 1
print("OR a | b =", a | b, "->", bits(a | b))
#Either 1 = 1
print()

#Part 3: Not & Xor
print("NOT ~a =", ~a & 0xFF, "->", bits(~a, 8))
#Flip all bits
print("XOR a ^ b =", a ^ b, "->", bits("a ^ b"))
#Different = 1
print()

#Part 4: Left/Right Shift
print("LEFT a << 1 =", a << 1, "->", bits(a * 2))
print("RIGHT a >> 1 =",a >> 1, "->", bits(a / 2))
print()

#Part 5: Odd or Even with Xor
print("Odd or Even")
for n in [7, 10, 15, 4]:
    result = "Even" if n ^ 1 == n + 1 else "Odd"
    print(n, "->", result)
print()

#Part 6: Count Bits
def count_bits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count

print("Bit count:")
for n in [a, b, 255]:
    print(n, "->", count_bits(n), "bits |", bits(n, count_bits(n)))