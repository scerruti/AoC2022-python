# Advent of Code - Day 9 - Part One

def up(knot):
    return knot[0], knot[1] + 1


def down(knot):
    return knot[0], knot[1] - 1


def right(knot):
    return knot[0] + 1, knot[1]


def left(knot):
    return knot[0] - 1, knot[1]


process = {'U' : up, 'D': down, 'R': right, 'L': left}


def distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def moveTo(actor, target):
    if actor[0] == target[0] or actor[1] == target[1]:
        if abs(actor[0] - target[0]) > abs(actor[1] - target[1]):
            return actor[0] - 1 if actor[0] > target[0] else actor[0] + 1, actor[1]
        elif abs(actor[0] - target[0]) < abs(actor[1] - target[1]):
            return actor[0], actor[1] - 1 if actor[1] > target[1] else actor[1] + 1
    else:
        return actor[0] - 1 if actor[0] > target[0] else actor[0] + 1, actor[1] - 1 if actor[1] > target[1] else actor[1] + 1


def result(input):
    moves = set()
    head = (0, 0)
    tail = (0, 0)
    minx = 0
    miny = 0
    for line in input:
        # print(line, end=' ')
        direction, steps = line.split(' ')
        for _ in range(int(steps)):
            head = process[direction](head)
            # print(head, end=' ')
            if distance(head, tail) > 1:
                tail = moveTo(tail, head)
                moves.add(tail)
            # print(tail)


    return len(moves)
