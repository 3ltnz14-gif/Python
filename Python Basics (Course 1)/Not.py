a = 10
b = 12
c = 12

print(a != b)
print(b != c)

a = "Python"
b = "coding"

if a != b:
    print("{0} and {1} are different." .format(a, b))

a = 4
b = 5

if (a == 1) != (b == 5):
    print("Hello!")

a = int(input("Enter a number\n-->"))

if a%2 != 0:
    print("{0} is not an even number." .format(a))
else:
    print("{0} is an even number." .format(a))