import turtle

turtle.speed(0)


def draw_square():
    turtle.pendown()
    turtle.pencolor("red")
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)


for i in range(16):
    draw_square()
    turtle.right(22.5)
