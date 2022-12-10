# Advent of Code - Day 10 - Part Two
screen = ['.'*40]*6


def display(clock, x):
    global screen
    pixel = (clock - 1) % 40 + 1
    line = (clock - 1) // 40
    print(line,pixel, x, x <= pixel <= x + 2)
    if x <= pixel <= x + 2:
        screen[line] = screen[line][:pixel-1]+"#"+screen[line][pixel:]


def result(input):
    x = 1
    clock = 1
    for line in input:
        if line[0:4] == 'noop':
            display(clock, x)
            clock += 1
        else:
            y = int(line.split()[1])
            display(clock, x)
            clock += 1
            display(clock, x)
            clock += 1
            x += y

    print()
    for i in range(6):
        print(screen[i])

    return 0
