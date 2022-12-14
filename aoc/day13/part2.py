# Advent of Code - Day 13 - Part Two
from functools import cmp_to_key
from part1 import correct_order

def result(input):
    packets = [eval(packet) for packet in input if packet]
    packets.extend([[[2]],[[6]]])

    sorted_packets = sorted(packets, key=cmp_to_key(correct_order))
    # bubble_sort(packets)

    sorted_packets.reverse()
    two = sorted_packets.index([[2]]) + 1
    six = sorted_packets.index([[6]]) + 1
    print(two, six, sorted_packets)
    return two*six


# Python program for implementation of Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if correct_order(arr[j], arr[j + 1]) <= 0:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
