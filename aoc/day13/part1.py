# Advent of Code - Day 13 - Part One

# Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more
# comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.
#
# When comparing two values, the first value is called left and the second value is called right. Then:
#
# If both values are integers, the lower integer should come first. If the left integer
# is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
#
# If both values are lists, compare the first value of each list, then the second value,
# and so on. If the left list runs out of items first, the inputs are in the right order.
#
# If the right list runs out of items first, the inputs are not in the right order.
# If the lists are the same length and no comparison makes a decision about the order,
# continue checking the next part of the input.
# If exactly one value is an integer, convert the integer to a list which contains that
# integer as its only value, then retry the comparison. For example, if comparing [0,0,0]
# and 2, convert the right value to [2] (a list containing 2); the result is then found by
# instead comparing [0,0,0] and [2].
import math


def result(input):
    sum = 0

    for i in range(0, math.ceil(len(input)/3), 1):
        if (correct_order(eval(input[i*3]),eval(input[i*3+1])) > 0):
            # print("# ", i+1)
            sum += i + 1
        # print()

    return sum


def correct_order(part1, part2):
    print(part1, " vs ", part2)
    if type(part1) == int and type(part2) == int:
        return part2 - part1
    elif type(part1) == list and type(part2) == list:
        i = 0
        while i < len(part1) and i < len(part2):
            r = correct_order(part1[i], part2[i])
            if r != 0:
                return r
            i += 1
        if len(part1) == len(part2):
            return 0
        else:
            return len(part2) - len(part1)
    elif type(part1) == list:
        return correct_order(part1, [part2])
    else:
        return correct_order([part1], part2)

