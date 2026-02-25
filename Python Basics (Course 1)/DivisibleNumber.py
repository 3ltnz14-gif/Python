numn = int(input("Enter a number (Numerator): "))
numd = int(input("Enter a number (Denominator):"))

if numn % numd == 0:
    print("/n {0} is divisible by {1}." .format(str(numn), str(numd)))
else:
    print("/n {0} is not divisible by {1}." .format(str(numn), str(numd)))