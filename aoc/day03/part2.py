# Advent of Code - Day 3 - Part Two

def result(input):
    sum = 0
    for i in range(0, len(input), 3):
        a = [y for y in [x for x in input[i] if x in input[i+1]] if y in input[i+2]][0]
        if a > 'Z':
            sum += ord(a) - ord('a') + 1
        else:
            sum += ord(a) - ord('A') + 27
    return sum
