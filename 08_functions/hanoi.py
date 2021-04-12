def solve(disc, a, b, c):
    if disc == 0:
        return

    solve(disc - 1, a, c, b)
    move(a, c)
    solve(disc - 1, b, a, c)


def move(source, target):
    print(source + " --> " + target)


# solve(number of discs, source, middle, target)
solve(3, 'A', 'B', 'C')
