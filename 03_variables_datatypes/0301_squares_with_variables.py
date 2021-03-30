import turtle

turtle.speed(0)

number_of_squares     = 4
size_of_square        = 50
space_between_squares = 30

turtle.penup()
turtle.backward(160)
turtle.pendown()

for j in range(number_of_squares):
  for i in range(4):
    turtle.forward(size_of_square)
    turtle.right(90)

  turtle.penup()
  turtle.forward(size_of_square + space_between_squares)
  turtle.pendown()
