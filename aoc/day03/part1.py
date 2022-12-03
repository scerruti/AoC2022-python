# Advent of Code - Day 3 - Part One

def result(input):
    sum = 0
    for line in input:
        a = line[:len(line)//2]
        b = line[len(line)//2:]
        print(line,a,b)
        c = [x for x in b if x in a][0]
        if c > 'Z':
            sum += ord(c) - ord('a') + 1
        else:
            sum += ord(c) - ord('A') + 27
    return sum
