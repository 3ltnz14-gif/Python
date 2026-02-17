i = int(input("Enter a number\n--> "))

if i < 15:
    print("Your number is less than 15")
    print("I am in if")
elif i == 15:
    print("Your number is 15")
    print("I am in elif")
else:
    print("Your number is more than 15")
    print("I am in else")
print("I'm not in any block")