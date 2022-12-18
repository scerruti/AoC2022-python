# Advent of Code - Day 15 - Part One
import re

def result(input):
    target = 10 # 2000000
    return beacon_free(input, target)


def beacon_free(input, target):

    points = set()
    beacons = set()
    for line in input:
        x = re.split(r'=|,|:', line)
        _, sx, _, sy, _, bx, _, by = x
        sx = int(sx)
        sy = int(sy)
        bx = int(bx)
        by = int(by)

        distance = abs(sx - bx) + abs(sy - by)
        for i in range(distance - abs(sy - target) + 1):
            points.add(sx+i)
            points.add(sx-i)

        if by == target:
            beacons.add(bx)

    print(len(points), len(beacons))
    points -= beacons
    # p = list(points)
    # p.sort()
    # print(p)
    return len(points)