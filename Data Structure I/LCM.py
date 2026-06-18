oneortwo = int(input("Would you like to do the first or second way? (1 or 2)"))

if oneortwo != 1 and oneortwo != 2:
    print("Invalid input")
elif oneortwo == 1:
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
else:
    def hcf(smallest, largest):
        while smallest:
            store = smallest
            smallest = largest%smallest
            largest = store
        return largest
    largest = int(input("Enter the greater number:"))
    smallest = int(input("Enter the lesser number:"))
    lcm = int((smallest / hcf(smallest, largest))*largest)
    print("LCM is", lcm)