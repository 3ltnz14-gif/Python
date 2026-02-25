age = int(input("How old are you?\n"))

if age >= 10 and age <= 20:
    print("You are allowed in this class")
elif age > 100:
    print("You really aren't older than 100...right?")
else:
    print("Sorry, the age limit for this class is between 10-20.")