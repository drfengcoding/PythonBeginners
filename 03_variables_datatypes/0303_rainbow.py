import turtle

turtle.speed(5)
turtle.pensize(4)
colors = ["red","yellow","pink","green","purple","orange","blue","silver","tan","brown"]

space = 2
radius = 50

for i in range(0, len(colors)):
  turtle.pencolor(colors[i])
  turtle.left(90)
  turtle.circle(radius, 180)

  turtle.penup()
  turtle.left(90)
  turtle.forward((radius + space)*2)
  radius = radius + space * 2
  turtle.pendown()

