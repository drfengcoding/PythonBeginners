age = input("How old are you?")
try:
  left = 80 - int(age)
except ValueError:
  print("Please enter a number in digits!")
else:
  if int(age) > 80:
    print("You turned 80 years old " + str(int(age) - 80) + " years ago.")
  else:
    print("You have " + str(left) + " years left until you are 80!")

