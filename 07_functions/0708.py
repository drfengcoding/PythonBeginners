import turtle

turtle.speed(0)
colors = ['red', 'blue', 'yellow', 'purple', 'green', 'pink', 'orange']


def draw_shape(sides, color, size):
    turtle.pendown()
    turtle.pencolor(color)
    for j in range(sides):
        turtle.forward(size)
        turtle.right(360 / sides)


for i in range(16):
    draw_shape(5 + i, colors[i % len(colors)], 10 + i * 2)
    turtle.right(22.5)
