# Advent of Code - Day 12 - Part Two
from part1 import make_map
from part1 import make_track
from part1 import make_step

visited = []
map = []
track = []
end = 0

terminate = lambda touched, map : len([pos for pos in touched if map[pos[0]][pos[1]] == ord('a')]) == 0
elevation_check = lambda r, c, elevation, map : map[r][c] - elevation > - 2

def result(input):
    global map, track, end
    start, end, map = make_map(input, terminator=-1)
    track = make_track(end, map)

    touched = [end]
    k = 0
    while terminate(touched, map) and len(touched) > 0:
        k += 1
        touched = make_step(k, touched, track, map, elevation_check)
        # print(k, touched)

    return k

