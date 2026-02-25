a = int(input("Enter speed 1"))
b = int(input("Enter speed 2"))
c = int(input("Enter speed 3"))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b:
    print("%d is higher than %d and %d." %(avg, a, b))
elif avg > b and avg > c:
    print("%d is higher than %d and %d." %(avg, b, c))
elif avg > c and avg > a:
    print("%d is higher than %d and %d." %(avg, c, a))
elif avg > a:
    print("%d is higher than %d." %(avg, a))
elif avg > a:
    print("%d is higher than %d." %(avg, a))
elif avg > b:
    print("%d is higher than %d." %(avg, b))
elif avg > c:
    print("%d is higher than %d." %(avg, c))
else:
    print("Invalid Input!")