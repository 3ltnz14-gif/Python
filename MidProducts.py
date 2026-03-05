num = int(input("Enter the number to be checked: "))
t = num
numLen = 0

while t > 0:
    numLen += 1
    t //= 10

if numLen >= 4:
    numLen //=2
    chk = 0
    while num > 0:
        rem = num % 10
        if chk == numLen:
            midOne = rem
        elif chk == (numLen - 1):
            midTwo = rem
        num //= 10
        chk += 1
    prod = midOne * midTwo

    print("\nProduct of Mid Digits", str(midOne), "*", str(midTwo), "=", prod)

else:
    print("\nYour number needs to be more than 3 digits!")
    
