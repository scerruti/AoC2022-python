# Advent of Code - Day 6 - Part Two

def result(input):
    for code in input:
        for i in range(1, len(code)-13):
            chunk = set(code[i:i+14])
            if (len(chunk) == 14):
                print(i+14, code[i:i+14], chunk)
                break
    return 0
