# Advent of Code - Day 11 - Part One
import re
import itertools

class Operation:
    def __init__(self, operand):
        self.operand = operand

    @staticmethod
    def factory(line):
        parts = line.split(' ')
        operator = parts[6]
        operand = parts[7]

        if operand == 'old':
            if operator == '*':
                return Square(0)
        else:
            operand = int(operand)
            if operator == '+':
                return Increment(operand)
            elif operator == '*':
                return Multiply(operand)

        raise LookupError

    def operate(self, value):
        pass

    def __str__(self):
        return str(__class__)


class Increment(Operation):
    def operate(self, value):
        return value + self.operand


class Square(Operation):
    def operate(self, value):
        return value * value


class Multiply(Operation):
    def operate(self, value):
        return value * self.operand


class Monkey:
    def __init__(self, lines):
        self.number = int(re.split(r'\s|:', lines[0])[1])
        self.items = [int(item) for item in lines[1].split(': ')[1].split(',')]
        self.operation = Operation.factory(lines[2])
        self.operand = self.operation.operand
        self.test = int(lines[3].split('  Test: divisible by ')[1])
        self.true_monkey = int(lines[4].split('    If true: throw to monkey ')[1])
        self.false_monkey = int(lines[5].split('    If false: throw to monkey ')[1])
        self.business = 0

    def __str__(self):
        return f'Monkey {self.number}:\n' + \
            f'\tStarting items: {self.items}\n' + \
            f'\tOperation: {self.operation} + {self.operation.operand}\n' +\
            f'\tTest: divisible by {self.test}\n' +\
            f'\t\tIf true: throw to monkey {self.true_monkey}\n' +\
            f'\t\tIf false: throw to monkey {self.false_monkey}'


def throw_to(monkeys, number, item):
    for monkey in monkeys:
        if monkey.number == number:
            monkey.items.append(item)


def result(configuration):
    monkeys = []
    num_monkeys = len(configuration) // 7 + 1
    for m in range(num_monkeys):
        monkeys.append(Monkey(configuration[m * 7:m * 7 + 6]))

    tests = [monkey.test for monkey in monkeys]
    common_divisor = 1
    for test in tests:
        if common_divisor % test != 0:
            common_divisor *= test

    for i in range(10000):
        monkey_round2(monkeys, common_divisor)
        print("\r", i, end='', flush=True)
        if i == 0 or i == 19 or (i + 1) % 1000 == 0:
            print('\n',i, monkey_business(monkeys))

    # for monkey in monkeys:
    #     print(monkey)

    return monkey_business(monkeys)[0]*monkey_business(monkeys)[1]


def monkey_business(monkeys):
    result = [monkey.business for monkey in monkeys]
    result.sort(reverse=True)
    return result


def monkey_round1(monkeys):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.business += 1
            item = monkey.items.pop()
            item = monkey.operation.operate(item)
            item //= 3
            if item % monkey.test == 0:
                throw_to(monkeys, monkey.true_monkey, item)
            else:
                throw_to(monkeys, monkey.false_monkey, item)


def monkey_round2(monkeys, common_divisor):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.business += 1
            item = monkey.items.pop()
            item = monkey.operation.operate(item)
            item %= common_divisor
            if item % monkey.test == 0:
                throw_to(monkeys, monkey.true_monkey, item)
            else:
                throw_to(monkeys, monkey.false_monkey, item)