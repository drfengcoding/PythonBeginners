def minus(a, b):
    return a - b


def divide(a, b):
    return a / b


def sum(lst):
    sum = 0
    for l in lst:
        sum = sum + l
    return sum


x = 20
y = 10
if x - y == minus(x, y):
    print("minus function works")

if x / y == divide(x, y):
    print("divide function works")

lst = [1, 3, 5, 7, 9]
if 1 + 3 + 5 + 7 + 9 == sum(lst):
    print("sum function works")
