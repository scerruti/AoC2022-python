# # Advent of Code - Day 17 - Part One

board = {}


class Block:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def can_move_left(self):
        global board
        return self.x > 0 and ((self.x - 1, self.y) not in board or board[(self.x - 1, self.y)] == self.parent)

    def can_move_right(self):
        return self.x < 6 and ((self.x + 1, self.y) not in board or board[(self.x + 1, self.y)] == self.parent)

    def can_move_down(self):
        return self.y > 0 and ((self.x, self.y - 1) not in board or board[(self.x, self.y - 1)] == self.parent)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)

    def move_down(self):
        self.move(0, -1)


class Shape:

    def __init__(self, row):
        col = 2
        self.blocks = [Block(col + part[0], row + part[1], self) for part in self.parts]
        self.add_blocks()
        self.shift = {'<': self.move_left, '>': self.move_right}

    def can_move_left(self):
        return all([block.can_move_left() for block in self.blocks])

    def can_move_right(self):
        return all([block.can_move_right() for block in self.blocks])

    def can_move_down(self):
        return all([block.can_move_down() for block in self.blocks])


    def add_blocks(self):
        for block in self.blocks:
            board[(block.x, block.y)] = self

    def clear_blocks(self):
        for block in self.blocks:
            del board[(block.x, block.y)]

    def move_left(self):
        if self.can_move_left():
            self.clear_blocks()
            for block in self.blocks:
                block.move_left()
            self.add_blocks()

    def move_right(self):
        if self.can_move_right():
            self.clear_blocks()
            for block in self.blocks:
                block.move_right()
            self.add_blocks()

    def move_down(self):
        if self.can_move_down():
            self.clear_blocks()
            for block in self.blocks:
                block.move_down()
            self.add_blocks()
            return False, max([block.y for block in self.blocks])
        else:
            return True, max([block.y for block in self.blocks])

    def get_height(self):
        return max([block.y for block in self.blocks])


class Minus(Shape):
    def __init__(self, row):
        self.parts = [[0, 0], [1, 0], [2, 0], [3, 0]]
        super().__init__(row)


class Plus(Shape):
    def __init__(self, row):
        self.parts = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
        super().__init__(row)


class Seven(Shape):
    def __init__(self, row):
        self.parts = [[2, 2], [2, 1], [0, 0], [1, 0], [2, 0]]
        super().__init__(row)


class Ell(Shape):
    def __init__(self, row):
        self.parts = [[0, 0], [0, 1], [0, 2], [0, 3]]
        super().__init__(row)


class Square(Shape):
    def __init__(self, row):
        self.parts = [[0, 0], [0, 1], [1, 0], [1, 1]]
        super().__init__(row)


def result(jets):
    shapes = [Minus, Plus, Seven, Ell, Square]
    cycle = 0
    height = -1
    jet = 0
    prev_height = 0

    period = len(jets[0]) * len(shapes)
    number_of_periods = 1000000000000 // period
    remaining_iterations = 1000000000000 % period

    i = 0
    done = False
    heights = []
    p = 0
    repeating = False

    while not done:
        i += 1
        # Add shape
        current_shape = shapes[cycle](height + 4)
        cycle = (cycle + 1) % len(shapes)

        # Shift
        settled = False
        while not settled:
            current_shape.shift[jets[0][jet]]()
            jet = (jet + 1) % len(jets[0])
            settled, top = current_shape.move_down()

        height = max(top, height)

        if not repeating and (i - 5) % period == 0:
            heights.append(height)
            p += 1
            if p == 2:
                pattern = copy_board(height, 10)
                print_board(height, height - 10)
            elif p > 2:
                matching_pattern = copy_board(height, 10)
                if all([pattern[row] == matching_pattern[row] for row in range(10)]):
                    print(p)
                    print_board(height, height - 10)

                    period_length = p - 2
                    repeating = True
                    r = 0

        if repeating:
            print(remaining_iterations - r)
            if r == remaining_iterations:
                result = heights[0] + number_of_periods * period_length * (heights[2] - heights[1]) + height - heights[2] + 1
                print(r, result)
                done = True
            r += 1

    return result


def print_board(height, rows=-1):
    for row in range(height, rows, -1):
        print(row, ": |", end='')
        for col in range(7):
            print("#" if (col, row) in board else " ", end='')
        print("|")
    print()

def copy_board(height, rows=-1):
    result = ['' for _ in range(rows)]
    for row in range(0, rows):
        result[row] = ''
        for col in range(7):
            result[row] += "#" if (col, height-row) in board else " "
    return result
# rocks = [
#     [
#         '  @@@@ ',
#         '       ',
#         '       ',
#         '       '
#     ],
#     [
#         '   @   ',
#         '  @@@  ',
#         '   @   ',
#         '       ',
#         '       ',
#         '       '
#     ],
#     [
#         '    @  ',
#         '    @  ',
#         '  @@@  ',
#         '       ',
#         '       ',
#         '       '
#     ],
#     [
#         '  @    ',
#         '  @    ',
#         '  @    ',
#         '  @    ',
#         '       ',
#         '       ',
#         '       '
#     ],
#     [
#         '  @@   ',
#         '  @@   ',
#         '       ',
#         '       ',
#         '       '
#     ]
# ]
#
#
# def result(jets):
#     rock = 0
#     old_cave = ['1','2']
#     cave = ['#######']
#     jet = 0
#
#     print(0)
#
#     for i in range(2022):
#         # new rock
#
#         cave[:0] = rocks[rock]
#         rock = (rock + 1) % len(rocks)
#         # [print(layer) for layer in cave]
#         # print("----\n")
#         print('\r',i, len(cave), len(old_cave))
#         # input()
#
#         dropped = True
#         while dropped:
#             if i == 9:
#                 print(jet, jets[0][jet])
#             push(cave, jets[0][jet])
#             jet = (jet + 1) % len(jets[0])
#
#             dropped = drop(cave)
#
#             if i == 9:
#                 [print(layer) for layer in cave]
#                 print("\n")
#
#         if old_cave and len(old_cave) > len(cave):
#             [print(layer) for layer in old_cave]
#             print("\n")
#             [print(layer) for layer in cave]
#             print("\n")
#             quit()
#         old_cave = cave.copy()
#
#     return len(cave)-1
#
#
# def push(cave, jet):
#     if jet == '<':
#         push = -1
#         check_range = range(1,7)
#     else:
#         push = 1
#         check_range = range(0,6)
#
#     bottom_row = 0
#     while '@' not in cave[bottom_row]:
#         bottom_row += 1
#
#     while '@' in cave[bottom_row]:
#         bottom_row += 1
#
#     stuck = any([(cave[row][0] == '@' and push == -1) or
#                  (cave[row][6] == '@' and push == 1) or
#                  (cave[row][col] == '@' and cave[row][col+push] == '#')
#                  for col in check_range for row in range(0, bottom_row)])
#
#     if not stuck:
#         for row in range(0, bottom_row):
#             new_row = ''
#             for col in range(0, 7):
#                 if 0 <= col - push < 7 and cave[row][col - push] == '@':
#                     new_row += '@'
#                 elif cave[row][col] == '@':
#                     new_row += ' '
#                 else:
#                     new_row += cave[row][col]
#             cave[row] = new_row
#
#
# def drop(cave):
#     top_row = 0
#     while '#' not in cave[top_row]:
#         top_row += 1
#
#     bottom_row = 0
#     while '@' not in cave[bottom_row]:
#         bottom_row += 1
#
#     while '@' in cave[bottom_row]:
#         bottom_row += 1
#
#     if bottom_row < top_row:
#         del cave[bottom_row]
#         return True
#
#     if all([
#         cave[row][col] in (' ','@') or cave[row-1][col] in (' ','#')
#         for row in range(top_row, bottom_row + 1)
#         for col in range(7)
#     ]):
#         for row in range(bottom_row, 0, -1):
#             new_row = ''
#             for col in range(7):
#                 new_row += cave[row-1][col] if cave[row][col] == ' ' else cave[row][col]
#             cave[row] = new_row
#             cave[row-1] = cave[row-1].replace('@', ' ')
#         if '#' not in cave[0]:
#             del cave[0]
#     else:
#         for row in range(0, bottom_row):
#             cave[row] = cave[row].replace('@', '#')
#         return False
#     return True
#
