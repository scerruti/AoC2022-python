# Advent of Code - Day 6 - Part One

def result(input):
    for code in input:
        for i in range(1, len(code)-3):
            chunk = set(code[i:i+4])
            if (len(chunk) == 4):
                print(i+4, code[i:i+4], chunk)
                break
    return 0
