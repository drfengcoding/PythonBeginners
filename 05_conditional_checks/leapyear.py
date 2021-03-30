try:
  year = int(input("Which year you want to check? "))
except ValueError:
  print("Please enter a year number!")
else:
  if year % 400 == 0:
    print(str(year) + " is a leap year.")
  elif year % 100 ==0:
    print(str(year) + " is not a leap year.")
  elif year % 4 == 0:
    print(str(year) + " is a leap year.")
  else:
    print(str(year) + " is not a leap year.")

