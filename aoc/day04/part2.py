# Advent of Code - Day 4 - Part Two

def result(input):
    count = 0
    for line in input:
        pairs = [pair.split('-') for pair in line.strip().split(",")]
        nums = [int(num) for pair in pairs for num in pair]
        if not (nums[1] < nums[2] or nums[0] > nums[3]):
            count += 1
    return count
