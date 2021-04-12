import turtle

turtle.speed(0)


def draw_square(color):
    turtle.pendown()
    turtle.pencolor(color)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


for i in range(16):
    draw_square("blue")
    turtle.right(22.5)

turtle.exitonclick()
