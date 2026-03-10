import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)
poly = turtle.Turtle()
sides = int(input("Enter the amount of sides: (must be >2) "))
sidelength = 70
angle = 360 / sides
if sides > 2:
    for i in range(sides):
        poly.forward(sidelength)
        poly.right(angle)
else:
    print("It needs to have >2 sides! Restart")

turtle.done()