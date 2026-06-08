def conversion(n):
    decimal, i = 0, 0
    while(n != 0):
        dec = n % 10
        decimal = decimal + dec * pow(2, i)
        n //= 10
        i += 1
    print("Decimal:", decimal)

binary = int(input("Enter your binary: "))
conversion(binary)