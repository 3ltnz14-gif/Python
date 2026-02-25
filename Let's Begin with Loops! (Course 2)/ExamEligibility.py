print("Welcome to the survey!\nThis survey will determine if you are eligible for the exam.")

medcause = input("If you did not attend a few classes, did you have a medical condition? (Y/N):\n").strip().upper()

if medcause != "Y" and medcause != "N":
    print("Invalid input!\nRestart the program")
elif medcause == "Y":
    print("\nYou are allowed.")
else:
    atten = int(input("Enter your total attendance (%)\n"))

    if atten >= 75:
        print("\nYou are allowed.")
    else:
        print("\nSorry, you are not eligible to take this exam.")