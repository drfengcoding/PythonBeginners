import turtle

turtle.speed(0)

try:
  number_of_squares     = int(input("Number of squares: "))
  size_of_square        = int(input("Size of square: "))
  space_between_squares = int(input("Space between squares: "))
except ValueError:
  print("Please enter a number in digits!")
else:
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

