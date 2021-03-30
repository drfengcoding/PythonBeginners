try:
  fruits = int(input("How many fruits did you eat so far?"))
except ValueError:
  print("Please enter a number in digits!")
else:
  if fruits > 5:
    print("You are easting too much fruits.")
  elif fruits ==5:
    print("You are eating exactly the right amount!")
  else:
    print("You need to eat " + str(5-fruits) + " more.")

