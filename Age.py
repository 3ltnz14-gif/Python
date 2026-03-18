def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")

try:
    n = int(input("Enter your age: "))
    enterage(n)
except ValueError:
    print("Only positive integers are allowed")
except:
    print("Something is wrong")