num = int(input("Enter a number to detemine the length of:\n(Decimals will not be counted)\n"))

length = 0

while num > 0:
    length += 1
    num //= 10

print("Your number's length is", length)