def add(p, q):
    return p + q
def sub(p, q):
    return p - q
def mult(p, q):
    return p * q
def div(p, q):
    return p / q

print("Please select the operation:")
print("a: Add")
print("b: Subtract")
print("c: Multiply")
print("d: Divide")

choice = input("Please select the operation: a/b/c/d\n").lower()

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if choice == "a":
    print("{0} + {1} = {2}" .format(num1, num2 , add(num1, num2)))
elif choice == "b":
    print("{0} - {1} = {2}" .format(num1, num2 , sub(num1, num2)))
elif choice == "c":
    print("{0} x {1} = {2}" .format(num1, num2 , mult(num1, num2)))
elif choice == "d":
    print("{0} / {1} = {2}" .format(num1, num2 , div(num1, num2)))
else:
    print("Invalid input!")