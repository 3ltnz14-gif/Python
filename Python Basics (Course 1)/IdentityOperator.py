x = 5

if type(x) is int:
    print("true")
else:
    print("false")

x = 1.1

if type(x) is not float:
    print("true")
else:
    print("false")

x = 20
y = 20

if x is y:
    print("x and y have the same identity.")

y = 30

if x is not y:
    print("x and y have a different identity.")

x = True
y = True
if x is y:
    print("x and y have the same identity.")

x = "20"
y = 20

if x is y:
    print("x and y have the same identity.")