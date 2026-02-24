FOrC = int(input("Enter 1 for Fahrenheit, 2 for Celsius\n-->"))
if FOrC != 1 and FOrC != 2:
    print("You selected {0} instead of 1 or 2! Restart the program!" .format(FOrC))
    run = 0
else:
    run = 1

if run != 0:
    if FOrC == 1:
        temp = int(input("Enter the temperature in Fahrenheit:\n-->"))
        if temp > 90:
            print("Wear cotton clothes!")
        else:
            print("Wear normal clothes!")
    else:
        temp = int(input("Enter the temperature in Celsius:\n-->"))
        if temp > 32:
            print("Wear cotton clothes!")
        else:
            print("Wear normal clothes!")