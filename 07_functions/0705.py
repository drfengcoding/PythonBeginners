import turtle

turtle.speed(0)


def draw_square(color, size):
    turtle.pendown()
    turtle.pencolor(color)
    for j in range(4):
        turtle.forward(size)
        turtle.right(90)


for i in range(16):
    draw_square("blue", 20 + i * 10)
    turtle.right(22.5)
