# Advent of Code - Day 10 - Part One

sum = 0
def report(clock, x):
    global sum
    if (clock + 20) % 40 == 0:
        print (clock, x, clock * x)
        sum += clock * x


def result(input):
    x = 1
    clock = 1
    for line in input:
        if line[0:4] == 'noop':
            report(clock, x)
            clock += 1
        else:
            y = int(line.split()[1])
            report(clock, x)
            clock += 1
            report(clock, x)
            clock += 1
            x += y
    return sum
