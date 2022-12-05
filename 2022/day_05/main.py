import re
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def parse_stacks(data: str) -> list[list[str]]:
    """Parse crate stacks part of data."""
    stacks = data.splitlines()
    positions = stacks.pop()

    result = []
    max_position = int(positions.split()[-1])
    for i in range(1, max_position + 1):
        pos = positions.index(str(i))
        result.append([])

        for line in stacks:
            value = line[pos] if len(line) >= pos else ' '
            if value != ' ':
                result[-1].append(line[pos])

    return result


def parse_moves(data: str) -> list:
    """Parse move commands part of data."""
    return [
        list(map(int, re.findall('[0-9]+', move)))
        for move in data.splitlines()
    ]


def parse_data(data: str) -> tuple[list, list]:
    """Parse data."""
    data_s, data_m = data.split('\n\n')
    return parse_stacks(data_s), parse_moves(data_m)


def move_crates(stacks: list, src: int, dst: int, amount: int) -> None:
    """Move pack of crates from src to dst."""
    to_move, stacks[src] = stacks[src][:amount], stacks[src][amount:]
    stacks[dst] = to_move + stacks[dst]


def get_result_code(stacks: list) -> str:
    """Get puzzle result."""
    return ''.join(s[0] for s in stacks)


def get_cratemover_9000_result(data: str) -> str:
    """Get result for puzzle part 1."""
    stacks, commands = parse_data(data)

    for amount, src, dst in commands:
        for _ in range(amount):
            move_crates(stacks, src - 1, dst - 1, 1)

    return get_result_code(stacks)


def get_cratemover_9001_result(data: str) -> str:
    """Get result for puzzle part 2."""
    stacks, commands = parse_data(data)

    for amount, src, dst in commands:
        move_crates(stacks, src - 1, dst - 1, amount)

    return get_result_code(stacks)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_cratemover_9000_result(input_data)}')
        print(f'Your result (2): {get_cratemover_9001_result(input_data)}')
