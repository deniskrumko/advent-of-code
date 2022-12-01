from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'


def count_calories(data: str) -> list[int]:
    """Count calories per elf."""
    return [
        sum(int(v) for v in line.split())
        for line in data.split('\n\n')
    ]


def max_calories(data: str) -> int:
    """Find max calories in data."""
    return max(count_calories(data))


def top_calories(data: str, top: int = 3) -> int:
    """Get sum of top 3 calories in data."""
    return sum(sorted(count_calories(data))[-top:])


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {max_calories(input_data)}')
        print(f'Your result (2): {top_calories(input_data)}')
