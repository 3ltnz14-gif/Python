num = int(input("Enter the number you would like to calculate to power of: "))
pw = int(input("Enter the power:"))

g = 1

for n in range(pw):
    g *= num
    print(n, g)