# Advent of Code - Day 1 - Part One

def result(input):
    max = 0
    sum = 0
    for line in input:
        if not line:
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line)

    if sum > max:
        max = sum

    return max
