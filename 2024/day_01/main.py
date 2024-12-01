from collections import Counter
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


# def parse_data(data: str):
#     """How I originally solved problem."""
#     list_a, list_b = [], []
#     for line in data.splitlines():
#         a, b = line.split()
#         list_a.append(int(a))
#         list_b.append(int(b))

#     return list_a, list_b


def parse_data(data: str, values_in_line: int = 2):
    """How I refactored to generators.

    Looks scary... But totally lazy.
    """
    def make_gen(pos: int):
        return (int(line.split()[pos]) for line in data.splitlines())

    return (make_gen(pos=pos) for pos in range(values_in_line))


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(
        abs(pair[0] - pair[1])
        for pair in zip(*(sorted(lst) for lst in parse_data(data)))
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    list_a, list_b = parse_data(data)
    count_b = Counter(list_b)
    return sum(a * count_b.get(a, 0) for a in list_a)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
