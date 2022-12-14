# Advent of Code - Day 12 - Part One
visited = []
map = []
track = []
end = 0

terminate = lambda touched, map : end not in touched
elevation_check = lambda r, c, elevation, map : map[r][c] - elevation < 2

def result(input):
    global map, track, end
    start, end, map = make_map(input)
    track = make_track(start, map)

    touched = [start]
    k = 0
    while terminate(touched, map) and len(touched) > 0:
        k += 1
        touched = make_step(k, touched, track, map, elevation_check)

    return k


def make_track(start, map):
    track = []
    for i in range(len(map)):
        track.append([])
        for j in range(len(map[i])):
            track[-1].append(0)
    i, j = start
    track[i][j] = 1
    return track


def make_step(k, touched, track, map, elevation_check):
    new_touched = []
    for i,j in touched:
        if track[i][j] == k:
            elevation = map[i][j]
            if elevation_check(i-1, j, elevation, map) and track[i-1][j] == 0:
                track[i-1][j] = k + 1
                new_touched.append((i-1, j))
            if elevation_check(i+1, j, elevation, map) and track[i+1][j] == 0:
                track[i+1][j] = k + 1
                new_touched.append((i+1, j))
            if elevation_check(i, j-1, elevation, map)  and track[i][j-1] == 0:
                track[i][j-1] = k + 1
                new_touched.append((i, j-1))
            if elevation_check(i, j+1, elevation, map) and track[i][j+1] == 0:
                track[i][j+1] = k + 1
                new_touched.append((i, j+1))
    return new_touched


def make_map(input, terminator=999):
    start = end = -1
    map = [[ord(letter) for letter in line] for line in input]
    map.insert(0, [terminator for _ in range(len(map[0]) + 1)])
    map.append([terminator for _ in range(len(map[0]) + 1)])

    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == ord('S'):
                start = (row, col+1)
                map[row][col] = ord('a')
            elif map[row][col] == ord('E'):
                end = (row, col+1)
                map[row][col] = ord('z')
        map[row].insert(0, terminator)
        map[row].append(terminator)

    return start,end, map


