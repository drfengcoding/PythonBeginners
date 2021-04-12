def factorial(number):
    if number == 0:
        print("return 1")
        return 1
    else:
        print("calling {}*f({})".format(number, number-1))
        return number * factorial(number - 1)


n = int(input("Give me a number to calculate the factorial: "))
print(factorial(n))
