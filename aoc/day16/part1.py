# Advent of Code - Day 16 - Part One
import re

def result(input):
    p = re.compile('Valve (?P<valve>[A-Z]+) has flow rate=(?P<rate>\d+); tunnel(?:s)? lead(?:s)? to valve(?:s)? (?P<neighbors>[A-Z]+((?:\,\s)[A-Z]+)*)')

    tunnels = {}
    for line in input:
        m = p.match(line)
        valves = [valve.replace(',','') for valve in m.group(3).split()]
        tunnels[m.group(1)] = [int(m.group(2)), valves, False]
    print(tunnels)

    time = 0
    total_flow = 0

    print(traverse(tunnels, 'AA', time, total_flow))

    return 0


def traverse(tunnels, current_node, time, total_flow, visited=[]):
    # Stop Loops
    if (current_node, total_flow) in visited or time >= 30:
        return -1

    print(current_node, total_flow, visited)
    time += 1
    if tunnels[current_node][0] != 0 and current_node not in [node for node, flow in visited]:
        total_flow += tunnels[current_node][0]  * (30 - time)
        print('\t', current_node, tunnels[current_node][0], (30 - time), total_flow)
        time += 1
    visited.append((current_node, total_flow))


    max_flow = 0
    for node in tunnels[current_node][1]:
        flow = traverse(tunnels, node, time, total_flow, visited.copy())
        max_flow = max(flow, max_flow)

    total_flow += max_flow
    return total_flow, time

