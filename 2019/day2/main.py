import operator

__all__ = (
    'intcode_computer',
    'intcode_to_list',
    'intcode_to_str',
)

optcodes = {
    1: operator.add,
    2: operator.mul,
}


def intcode_to_list(data) -> list:
    """Convert string intcode to list."""
    return [int(value) for value in data.split(',')]


def intcode_to_str(data) -> str:
    """Convert list intcode to string."""
    return ','.join(str(value) for value in data)


def intcode_computer(intcode: list) -> str:
    """Mighty intcode computer."""
    position, optcode = 0, 0

    while True:
        cursor = intcode[position]
        if cursor == 99:
            break

        optcode = optcodes.get(cursor)
        if not optcode:
            break

        a = intcode[position + 1]
        b = intcode[position + 2]
        c = intcode[position + 3]
        intcode[c] = optcode(intcode[a], intcode[b])
        position += 4

    return intcode


def run_intcode(input_file: str, a: int, b: int) -> int:
    """Run intcode and get first position value."""
    with open(input_file, 'r') as f:
        intcode = intcode_to_list(data=f.readline())
        intcode[1] = a
        intcode[2] = b
        return intcode_computer(intcode)[0]


def find_values(input_file: str, expected: int) -> tuple:
    """Find A and B values that matches expected."""
    for i in range(100):
        for j in range(100):
            if run_intcode(input_file, i, j) == expected:
                return i, j

    print('Cannot find pair of values')
    return None, None


if __name__ == '__main__':
    input_file = '2019/day2/input.txt'
    print(f'Input file: {input_file}')
    print(f'First value: {run_intcode(input_file, a=12, b=2)}')

    a, b = find_values(input_file, 19690720)
    print(f'Pair of values: a={a}, b={b}')
    print(f'Result value: {100 * a + b}')
