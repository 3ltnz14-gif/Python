n = int(input("Enter a whole number greater than 1"))

#Print the numbers from n to 1
print("Numbers from {0} to {1} are: " .format(n, 1))

#for loop to print numbers

for i in range(n, 0, -1):
    print("{0}, " .format(i))
