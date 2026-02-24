print("Enter marks obtained in 5 subjects (/100)")

m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

tot = m1 + m2 + m3 + m4 + m5
avg = tot/5

if avg == 100:
    print("You got a perfect score! A+")
elif avg>= 91 and avg<=99:
    print("A-")
elif avg>= 81 and avg<=90:
    print("A-")
elif avg>= 71 and avg<=80:
    print("B+")
elif avg>= 66 and avg<=70:
    print("B-")
elif avg>= 61 and avg<=65:
    print("C+")
elif avg>= 56 and avg<=60:
    print("C-")
elif avg>= 51 and avg<=55:
    print("D+")
elif avg>= 46 and avg<=50:
    print("D-")
elif avg>= 41 and avg<=45:
    print("E")
elif avg<=40:
    print("F")
else:
    print("Invalid Input!")