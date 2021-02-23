import turtle

turtle.speed(0)
turtle.penup()
turtle.backward(160)
turtle.pendown()

for j in range(10):
  for i in range(4):
    turtle.forward(50+j*10)
    turtle.right(90)
