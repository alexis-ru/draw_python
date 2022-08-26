import turtle
import random

windows = turtle.Screen()
windows.setup(1100, 750)
windows.bgcolor('light green')


def cirls(y):
    pen = turtle.Turtle()
    if y < 0:
        pen.color('blue')
        pen.shape('arrow')
        pen.pensize(8)
    else:
        pen.color('green')
        pen.shape('turtle')
        pen.pensize(3)
    for pos_x in [-200, 0, 200]:
        pen.penup()
        pen.setpos(x=pos_x, y=y)
        pen.pendown()
        pen.circle(radius=random.randint(50, 100))
        pen.forward(100)


cirls(100)
cirls(-100)



# for circle shape
turtle.shape("circle")
turtle.penup()
turtle.setpos(x=100, y=-150)
turtle.pendown()
turtle.color('orange')
turtle.pensize(2)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)

turtle.right(60)
turtle.forward(100)



turtle.penup()
turtle.setpos(x=-300, y=-150)
turtle.pendown()
turtle.shape("triangle")
turtle.color('purple')
turtle.pensize(4)
for _ in range(10):
    turtle.forward(100)
    turtle.right(360 / 10)


windows.mainloop()
