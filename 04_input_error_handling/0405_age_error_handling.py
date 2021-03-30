age = input("How old are you?")
try:
  left = 80 - int(age)
except ValueError:
  print("Please enter a number in digits!")
else:
  print("You have " + str(left) + " years left until you are 80!")

