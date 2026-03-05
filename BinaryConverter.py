def convert(n):
    if n > 1:
        convert(n//2)
    print(n % 2, end = "")

dec = int(input("Enter a number to be converted: "))

convert(dec)
