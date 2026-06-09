a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    highest = a
else:
    highest = b
print(f"LCM of {a} and {b}:")
for i in range(highest, (a*b) + 1):
    if i % a == 0 and i % b == 0:
        print(f">{i}")
        break

