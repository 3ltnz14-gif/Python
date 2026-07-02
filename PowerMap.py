items = ["A", "B", "C"]
n = len(items) #(3)
total = 2 ** n
print("=== Power Map: ===")
print(f"Items = {items}\nElements = {n}\nTotal subsets = {total}")
mask = 0
print(f"Mask table (n = {n})")
while mask < total:
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1
    print(f"Mask #: {mask} Bits = {bit2} {bit1} {bit0}")
    mask += 1

mask = 0
print("All subsets (bit probe):")
while mask < total:
    subset = []
    j = 0
    while j < n:
        probe = 1 << j
        if (mask & probe) != 0:
            subset.append(items[j])
        j += 1
    print(f"Mask {mask} -> {subset}")
    mask += 1

def bit_diff(a, b):
    flips = 0
    while a > 0 or b > 0:
        last_a = a & 1
        last_b = b & 1
        if last_a != last_b:
            flips += 1
        a >>= 1
        b >>= 1
    return flips
print("Bit difference:")
print(f"bit_diff(12, 15) = {bit_diff(12, 15)}    (12={bin(12)}, 15={bin(15)})")
print(f"bit_diff(21, 24) = {bit_diff(21, 24)}    (21={bin(21)}, 24={bin(24)})")
print(f"bit_diff(8, 8)   = {bit_diff(8, 8)}    (12={bin(12)}, 15={bin(15)})")