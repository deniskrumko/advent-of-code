from itertools import product
from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def unfold_line(line: str) -> str:
    x, groups = line.split()
    return '?'.join([x] * 5) + ' ' + ','.join(groups.split(',') * 5)


def replace_with(line: str, replacements: list) -> str:
    """Replace all '?' with replacements."""
    for r in replacements:
        line = line.replace('?', r, 1)
    return line


def count_defected_groups(line: str) -> list[int]:
    """Count defected groups in a line."""
    return [len(gr) for gr in line.split('.') if gr != '']


def get_arrangements(line: str) -> set[str]:
    """Get all possible arrangements for a line."""
    x, groups = line.split()
    found = set()
    groups = [int(g) for g in groups.split(',')]
    for pr in product('.#', repeat=x.count('?')):
        newLine = replace_with(x, pr)
        newGroups = count_defected_groups(newLine)
        if newGroups == groups:
            found.add(newLine)
    return found


def function_1(data: str) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(len(get_arrangements(line)) for line in data.splitlines())


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return sum(len(get_arrangements(unfold_line(line))) for line in data.splitlines())


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
