from itertools import combinations
from typing import (
    List,
    Union,
)


def parse_input_data(input_data: str) -> List[int]:
    """Convert input data string to list"""
    return [int(value) for value in input_data.strip().split('\n')]


def get_incorrect_value(input_data: Union[str, list], preamble: int = 25) -> int:
    """Find first incorrect value in integers list."""
    values = parse_input_data(input_data) if isinstance(input_data, str) else input_data
    for i in range(preamble, len(values)):
        if not any(a + b == values[i] for a, b in combinations(values[i - preamble:i], 2)):
            return values[i]

    raise ValueError('Input data has no incorrect values!')


def get_encryption_weakness(input_data: str, preamble: int = 25) -> int:
    """Find encryption weakness in input data."""
    values = parse_input_data(input_data)
    size = len(values)
    incorrect_value = get_incorrect_value(values, preamble=preamble)

    for i in range(size):
        for j in range(i + 1, size):
            block = values[i:j]
            block_sum = sum(block)
            if block_sum == incorrect_value:
                return min(block) + max(block)
            elif block_sum > incorrect_value:
                break

    raise ValueError('Input data has no encryption weakness!')


if __name__ == '__main__':
    with open('2020/day_09/input.txt', 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_incorrect_value(input_data)}')
        print(f'Your result (2): {get_encryption_weakness(input_data)}')
