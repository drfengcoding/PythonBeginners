try:
  year = int(input("Which year you want to check? "))
except ValueError:
  print("Please enter a year number!")
else:
  is_leap_year = False
  if year % 400 == 0:
    is_leap_year = True
  elif year % 100 != 0 and year % 4 == 0:
    is_leap_year = True

  if is_leap_year == True:
    print(str(year) + " is a leap year.")
  else:
    print(str(year) + " is not a leap year.")
    while is_leap_year == False:
      year = year + 1
      if year % 400 == 0:
        is_leap_year = True
      elif year % 100 != 0 and year % 4 == 0:
        is_leap_year = True
      if is_leap_year == True:
        print("The next leap year is " + str(year))

