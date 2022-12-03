# Advent of Code - Day 2 - Part Two

def result(input):
    total = 0
    for line in input:
        a,x = line.split(' ')
        a = ord(a) - ord('A')
        x = ord(x) - ord('X')
        b = (a + x - 1) % 3

        round = b + 1
        win = (b - a + 4) % 3 - 1

        total += round + 3 + 3 * win

    return total