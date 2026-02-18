c = input("Enter a Character\n-->")

if c>="0" and c<="9":
    print("\nIt is a number.")
elif c>="a" and c<="z":
    print("\nIt is a letter")
elif c>="A" and c<="A":
    print("\nIt is a letter")
else:
    print("\nIt is a special character")