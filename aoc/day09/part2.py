# Advent of Code - Day 9 - Part Two

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
    moves = set((0,0))
    knots = [(0, 0) for _ in range(10)]
    print(knots)
    for line in input:
        # print(line, end=' ')
        direction, steps = line.split(' ')
        for _ in range(int(steps)):
            knots[0] = process[direction](knots[0])

            for k in range(1, 10):
                # print(head, end=' ')
                if distance(knots[k-1], knots[k]) > 1:
                    knots[k] = moveTo(knots[k], knots[k-1])
                    if k == 9:
                        moves.add(knots[k])
            # print(tail)


    return len(moves)
