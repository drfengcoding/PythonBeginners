import turtle

turtle.speed(0)

length = 30

try:
    sides = int(input("How many sides? "))
    angle = 360/sides
except ValueError:
  print("Please enter a number in digits!")
else:
  for i in range(sides):
      turtle.forward(length)
      turtle.left(angle)

