# Advent of Code - Day 8 - Part One
trees = []

def result(input):
    global trees
    for row in input:
        trees.append([int(tree) for tree in row])

    count = len(trees) * 2 + (len(trees) - 2) * 2
    for row in range(1, len(trees) - 1):
        for col in range(1, len(trees[row]) - 1):
            if tallest(row, col, -1, 0) or tallest(row, col, 1, 0) or tallest(row, col, 0, 1) or tallest(row, col, 0, -1):
                count += 1
    print(count)

    max = 0
    for row in range(0, len(trees)):
        for col in range(0, len(trees[row])):
            temp = scenic_view(row, col)
            if temp > 30:
                print(temp, row, col)
            if temp > max:
                max = temp
    print(max)


def scenic_view(row, col):
    return count(row, col, -1, 0) * count(row, col, 1, 0) * count(row, col, 0, 1) * count(row, col, 0, -1)


def count(row, col, dr, dc):
    view = 0
    r = row
    c = col
    print('\t'+str(trees[r][c]), end=' ')
    while 0 <= r+dr < len(trees) and 0 <= c+dc < len(trees[row]):
        print(trees[r+dr][c+dc], end=' ')
        if trees[row][col] <= trees[r+dr][c+dc]:
            view += 1
            print(" = " + str(view))
            return view
        view += 1
        r += dr
        c += dc
    print(" = " + str(view))
    return view


def tallest(row, col, dr, dc):
    r = row + dr
    c = col + dc
    while 0 <= r < len(trees) and 0 <= c < len(trees[row]):
        # print(r, c)
        if trees[r][c] >= trees[row][col]:
            return False
        r += dr
        c += dc
    return True