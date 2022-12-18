# Advent of Code - Day 15 - Part Two
import re

def result(input):
    s = []
    b = []

    for line in input:
        x = re.split(r'=|,|:', line)
        _, sx, _, sy, _, bx, _, by = x
        s.append((int(sx), int(sy), abs(int(sx) - int(bx)) + abs(int(sy) - int(by))))
        b.append((int(bx), int(by)))


    for row in range(4000000):
        ranges = []
        for sx, sy, distance in s:
            fill = distance - abs(sy - row)
            if fill > 0:
                start = max(0, sx - fill)
                end = min(sx + fill, 4000000)
                ranges.append([start, end])

        for bx, by in b:
            if by == row and 0 <= bx < 4000000:
                ranges.append([bx, bx])

        intervals = mergeIntervals(ranges)
        if len(intervals) > 1:
            freq = (intervals[0][1] + 1) * 4000000 + row
            print("Row: ", row, intervals, freq)

    return 0


def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    return stack