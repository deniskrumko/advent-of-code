from functools import reduce
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def get_extrapolated_value(values: list[int], left: bool = False) -> int:
    """Calculate extrapolated value for values."""
    history = [values]
    while set(values) != {0}:
        values = [values[i] - values[i - 1] for i in range(1, len(values))]
        history.append(values)

    return (
        reduce(lambda a, b: b - a, [h[0] for h in reversed(history)])  # Get left value
        if left else
        sum(h[-1] for h in history)  # Get right value
    )


def function_1(data: str, left: bool = False) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(
        get_extrapolated_value([int(v) for v in line.split()], left=left)
        for line in data.splitlines()
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data, left=True)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
