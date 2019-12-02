import operator


def operators_map(comp):
    op_map = {
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        'inc': operator.add,
        'dec': operator.sub
    }
    return op_map[comp]


def main():
    with open('day8/input.txt', 'r') as f:
        puzzle = f.readlines()

    registers = {}

    max_highest_value = 0

    for line in puzzle:
        reg1, action, value1, _if, reg2, compare, value2 = line.split()

        registers.setdefault(reg1, 0)
        registers.setdefault(reg2, 0)

        if operators_map(compare)(registers[reg2], int(value2)):
            registers[reg1] = operators_map(action)(
                registers[reg1], int(value1)
            )

        highest_value = max(list(registers.values()))

        if highest_value > max_highest_value:
            max_highest_value = highest_value

    print(highest_value)
    print(max_highest_value)


if __name__ == '__main__':
    main()
