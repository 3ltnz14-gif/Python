number = int(input("Enter a number\n--> "))
print("The number to be checked is {0}" .format(number))

if (number % 2) == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")