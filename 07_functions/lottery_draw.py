import turtle
import random

turtle.hideturtle()

# generate a random number between 1 and 37
def get_random_number():
  return random.randint(1, 37)

# define number format
def format_number(number):
  if number < 10:
      return '0' + str(number)
  else:
      return str(number)

while True:
  s = ""
  for i in range(6):
    s = s + format_number(get_random_number()) + ' '
  turtle.clear()
  turtle.write(s, move=False, align="center", font=("Times New Roman", 40, "bold"))




