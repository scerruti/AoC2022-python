# Advent of Code - Day 2 - Part One

def result(input):
    total = 0
    for line in input:
        a,x = line.split(' ')
        a = ord(a) - ord('A')
        x = ord(x) - ord('X')

        round = x + 1
        win = (x - a + 4) % 3 - 1

        total += round + 3 + 3 * win

    return total
