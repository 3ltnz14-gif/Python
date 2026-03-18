try:
    n1, n2 = eval(input("Enter two numbers, seperated by a comma. (e.g. 1, 2): "))
    r = n1 / n2
    print("Result is", r)
except ZeroDivisionError:
    print("Division by zero results in an error")
except SyntaxError:
    print("Wrong input")
except ValueError:
    print("It needs to be a number!")
else:
    print("No exceptions")
finally:
    print("This line will always execute.")