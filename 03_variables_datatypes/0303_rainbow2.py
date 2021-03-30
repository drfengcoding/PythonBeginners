import turtle

turtle.pensize(4)
colors = ["red", "yellow", "blue", "purple", "pink", "green", "orange"]
radius = 50
space = 5

for i in range(len(colors)):
  turtle.pencolor(colors[i])
  turtle.penup()
  turtle.left(90)
  turtle.pendown()

  if i%2 == 0:
    turtle.circle(radius + space*i, 180)
  else:
    turtle.circle(radius + space*i, -180)

  turtle.penup()
  turtle.right(90)
  turtle.forward(space)
