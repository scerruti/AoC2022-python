# Advent of Code - Day 14 - Part One

def result(input):
    cave = [['.']*1000 for _ in range(1000)]
    min_x = 999
    max_x = 0
    min_y = 999
    max_y = 0

    for rock_path in input:
        points = [(int(x),int(y)) for x,y in [point.split(',') for point in rock_path.split(' -> ')]]

        start = points[0]
        min_x = min(min_x, start[0])
        max_x = max(max_x, start[0])
        min_y = min(min_y, start[1])
        max_y = max(max_y, start[1])

        for i in range(1, len(points)):
            end = points[i]
            min_x = min(min_x, end[0])
            max_x = max(max_x, end[0])
            min_y = min(min_y, end[1])
            max_y = max(max_y, end[1])

            x_dir = 1 if end[0] >= start[0] else -1
            y_dir = 1 if end[1] >= start[1] else -1
            for x in range(start[0], end[0]+x_dir, x_dir):
                for y in range(start[1], end[1]+y_dir, y_dir):
                    cave[x][y] = '#'
            start = end

    grains = 0
    while True:
        pos = (500,0)
        moving = True

        while moving:
            if cave[pos[0]][pos[1]+1] == '.':
                pos = (pos[0], pos[1]+1)
            elif cave[pos[0]-1][pos[1]+1] == '.':
                pos = (pos[0]-1, pos[1]+1)
            elif  cave[pos[0]+1][pos[1]+1] == '.':
                pos = (pos[0]+1, pos[1]+1)
            else:
                cave[pos[0]][pos[1]] = 'o'
                moving = False

            if pos[1] > max_y:
                return grains

        grains += 1
        # print_cave(cave, min_x, min_y, max_x, max_y)

    print_cave(cave, min_x, min_y, max_x, max_y)


    return 0


def print_cave(cave, min_x, min_y, max_x, max_y):
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            print(cave[x][y], end='')
        print()
