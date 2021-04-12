import turtle

turtle.speed(0)


def draw_shape(sides, color, size):
    turtle.pendown()
    turtle.pencolor(color)
    for j in range(sides):
        turtle.forward(size)
        turtle.right(360 / sides)


for i in range(16):
    draw_shape(4 + i, "blue", 20 + i * 5)
    turtle.right(22.5)

turtle.exitonclick()