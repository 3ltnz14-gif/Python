try:
    n = int(input("Enter a number: "))
    print("The number entered is", n)
except ValueError as ex:
    print("Exception:", ex)