def is_leap_year(year):
    leap_year = False
    if year % 400 == 0:
        leap_year = True
    elif year % 100 != 0 and year % 4 == 0:
        leap_year = True
    return leap_year

    # simpler solution
    # return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def get_next_leap_year(year):
    while is_leap_year(year) == False:
        year = year + 1
    return year


try:
    year = int(input("Which year you want to check? "))
except ValueError:
    print("Please enter a year number!")
else:
    if is_leap_year(year):
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")
        print("The next leap year is " + str(get_next_leap_year(year)))
