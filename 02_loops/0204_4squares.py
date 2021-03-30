import turtle

turtle.penup()
turtle.backward(160)
turtle.pendown()

for j in range(4):
  for i in range(4):
    turtle.forward(50)
    turtle.right(90)

  turtle.penup()
  turtle.forward(80)
  turtle.pendown()
