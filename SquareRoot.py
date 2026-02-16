num = int(input("Enter number to square root: "))

num_sqrt = num ** 0.5
print(f"The Number Is {num} and its' square root is {num_sqrt}")

num = int(input("Enter another number to square root: "))

num_sqrt = num ** 0.5
print("The square root of %0.2f is {%0.3f}" % (num, num_sqrt))

num = 1
print(num)
num += 1
print(num, "+= 1")
num -= 1
print(num, "-= 1")
num *= 2
print(num, "*= 2")
num /= 2
print(num, "/= 2")
num += 8
print(num, "+= 8")
num **= 2
print(num, "**= 2")
num //= 2
print(num, "//= 2")