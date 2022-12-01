from collections import Counter
from functools import reduce


def get_differences(input_data: str) -> Counter:
    """Count differences between adapter values."""
    values = sorted([int(value) for value in input_data.strip().split('\n')], reverse=True)
    pairs = zip([max(values) + 3] + values, values + [0])
    return Counter(a - b for a, b in pairs)


def get_1_and_3_differences(input_data: str) -> int:
    """Multiply amount of 1 and 3 adapter differences."""
    diffs = get_differences(input_data)
    return diffs[1] * diffs[3]


def convert_input_data(input_data: str) -> list:
    """Convert input data string to list of values"""
    values = sorted([int(value) for value in input_data.strip().split('\n')])
    return [0] + values + [max(values) + 3]


def count_solutions_by_recursive(input_data: str) -> int:
    """Count all possible solutions using recursive.

    WARNING: This is bruteforce solution that works too long for large input data.
    """
    values: list = convert_input_data(input_data)

    def walk(position=0, counter=0):
        for jump in range(1, 4):
            new_value = values[position] + jump
            if new_value in values:
                counter = walk(values.index(new_value), counter)

        return counter + (position == (len(values) - 1))

    return walk()


def count_solutions(input_data: str) -> int:
    """Count all possible solutions using logic and math.

    Split values to groups of incrementing numbers. Then get amount of solutions per each group
    and multiply them to result. Amount of solutions per stack size added to `convert` dict, and
    so it happens, that input data has only 3 possible variants: 3, 4 or 5 numbers in a row.

    Example:
        Values are [0, 1, 2, 3, 6, 9, 10, 11]. Group A is [0, 1, 2, 3], group B is [9, 10, 11].
        Group A has 4 choices, group B has 2 choices. Result is 4 * 2 = 8.
    """
    if 2 in get_differences(input_data):
        raise ValueError('Input data cannot have jumps with value "2"')

    stack_sizes, stack = [], []
    for value in convert_input_data(input_data):
        if not stack or value - stack[-1] == 1:
            stack.append(value)
            continue

        if len(stack) > 2:
            stack_sizes.append(len(stack))
        stack = [value]

    convert = {3: 2, 4: 4, 5: 7}  # Calculated by hand because there are no formula
    return reduce(lambda x, y: x * y, [convert[i] for i in stack_sizes])


if __name__ == '__main__':
    with open('2020/day_10/input.txt', 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_1_and_3_differences(input_data)}')
        print(f'Your result (2): {count_solutions(input_data)}')
