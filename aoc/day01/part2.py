# Advent of Code - Day 1 - Part Two

def result(input):
    max = []
    sum = 0
    for line in input:
        if not line:
            max.append(sum)
            sum = 0
        else:
            sum += int(line)

    max.append(sum)
    max.sort(reverse=True)

    return max[0] + max[1] + max[2]