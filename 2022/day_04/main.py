from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def parse_data(data: str) -> list[list[list[int]]]:
    """Parse data to int pairs."""
    return [
        [[int(i) for i in x.split('-')] for x in line.split(',')]
        for line in data.splitlines()
    ]


def is_fully_overlapping_pair(a: list[int], b: list[int]) -> bool:
    """Check if pair is fully overlapping."""
    return any((x[0] <= y[0] and x[1] >= y[1]) for x, y in ((a, b), (b, a)))


def is_partially_overlapping_pair(a: list[int], b: list[int]) -> bool:
    """Check if pair is partially overlapping."""
    return any([
        *(b[0] <= _a <= b[1] for _a in a),
        *(a[0] <= _b <= a[1] for _b in b),
    ])


def count_fully_overlapping_pairs(data: str):
    """Get result for part 1 task."""
    return sum(is_fully_overlapping_pair(*p) for p in parse_data(data))


def count_partially_overlapping_pairs(data: str):
    """Get result for part 2 task."""
    return sum(is_partially_overlapping_pair(*p) for p in parse_data(data))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {count_fully_overlapping_pairs(input_data)}')
        print(f'Your result (2): {count_partially_overlapping_pairs(input_data)}')
