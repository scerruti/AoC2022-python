# Advent of Code - Day 7 - Part One

# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)
#
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

def compute_size(node):
    size = node['size']
    for child in node['child']:
        child['size'] = compute_size(child)
        size += child['size']
        print(child['name'], child['size'])

    print(node['name'], size)
    return size


def sum_of_small(node):
    result = 0
    for child in node['child']:
        result += sum_of_small(child)
    if node['size'] <= 100000:
        result += node['size']
    return result


def find_closest(node, at_least, so_far = 0):
    if so_far >= node['size'] >= at_least:
        so_far = node['size']

    for child in node['child']:
        so_far = find_closest(child, at_least, so_far)

    return so_far


def result(input):
    root = {"name": '/', "child": [], "size": 0, "parent": None}
    current = root
    for line in input:
        if (line[0] == '$'):
            if line[2:4] == 'ls':
                pass
            elif line[2:4] == 'cd':
                name = line[5:]
                if name == '..':
                    current = current['parent']
                else:
                    for node in current['child']:
                        if node['name'] == name:
                            current = node
        elif line[0:3] == 'dir':
            name = line[4:]
            current['child'].append({"name": name, "child": [], "size": 0, "parent": current})
            # print('name:', name)
        else:
            pos = line.index(" ")
            size = int(line[:pos])
            current['size'] += size
            # print('size:', size, line[pos:])

    root['size'] = compute_size(root)

    print("Part 1:",sum_of_small(root))

    delete_at_least = 47870454 - 40000000
    print("Part 2", find_closest(root, delete_at_least, 70000000))
