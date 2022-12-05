# Advent of Code - Day 5 - Part One

stacks = [[],[],[],[],[],[],[],[],[]]
# stacks = [[],[],[]]


def result(input):
    i = 0
    while input[i]:
        print(input[i])
        for j in range(len(stacks)):
            col = j * 4 + 1
            if len(input[i]) > col and not input[i][col] == ' ':
                if stacks[j]:
                    stacks[j].insert(0, input[i][col])
                else:
                    stacks[j] = [input[i][col]]
        i += 1

    for stack in stacks:
        stack.pop(0)

    print(stacks)

    for line in input[i+1:]:
        _, qty, _, src, _, dest = line.split(' ')
        qty = int(qty)
        src = int(src) - 1
        dest = int(dest) - 1

        crates_to_move = stacks[src][-1 * qty:]
        # crates_to_move.reverse()
        print(crates_to_move)
        stacks[dest].extend(crates_to_move)
        stacks[src] = stacks[src][:-1 * qty:]
        print(stacks)

    code = ''
    for stack in stacks:
        code += stack[-1]

    return code
