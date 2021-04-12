import turtle, datetime, time

turtle.hideturtle()


def clock():
    while True:
        turtle.clear()
        current_time = datetime.datetime.now()
        turtle.write(current_time.strftime("%H:%M:%S"), move=False, align="center",
                     font=("Times New Roman", 40, "bold"))
        time.sleep(1)


clock()
