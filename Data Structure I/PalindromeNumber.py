number = int(input("Enter your number: "))

originalnum = number
reversednum = 0

while number > 0:
    digit = number % 10
    reversednum = reversednum * 10 + digit
    number //= 10

if originalnum == reversednum:
    print(f"{originalnum} is a palindrome")
else:
    print(f"{originalnum} is not a palindrome")