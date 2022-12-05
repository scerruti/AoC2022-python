# Advent of Code - Day 4 - Part One

def result(input):
    count = 0
    for line in input:
        pairs = [pair.split('-') for pair in line.strip().split(",")]
        nums = [int(num) for pair in pairs for num in pair]
        if nums[0] <= nums[2] and nums[1] >= nums[3] or nums[2] <= nums[0] and nums[3] >= nums[1]:
            count += 1
    return count
