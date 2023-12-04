import re
from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def count_winning_numbers(line: str) -> int:
    """Counts how much of numbers in line have won."""
    m = re.match(r'^Card\s+\d+: (?P<win>[\d\s]+) \| (?P<have>[\d\s]+)$', line).groupdict()
    make_set = lambda key: set(int(v) for v in m[key].split())  # noqa (it's bad, sorry)
    return len(make_set('win') & make_set('have'))


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(
        int(pow(2, count_winning_numbers(line) - 1))
        for line in data.splitlines()
    )


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    cards_dict = defaultdict(lambda: 1)  # counts copies of each card
    for i, line in enumerate(data.splitlines(), 1):
        winning = count_winning_numbers(line)
        i_count = cards_dict[i]  # this line is needed to init defaultdict
        for j in range(1, winning + 1):
            cards_dict[i + j] += i_count
    return sum(cards_dict.values())


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
