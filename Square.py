import turtle
turtle.Screen().bgcolor("light blue")
turtle.Screen().title("Turtle")
pen = turtle.Turtle()
pen.speed("fast")

for i in range(4):
    pen.forward(100)
    pen.left(90)

turtle.done()