lower = int(input("Enter the number to start: "))
upper = int(input("Enter the number to end: "))
print("Prime numbers between", lower, "and", upper, "are:\n")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
