import turtle

turtle.speed(0)
turtle.pendown()
turtle.pencolor("red")

for i in range(16):
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(22.5)
